from django.shortcuts import render, get_object_or_404,redirect
from .models import Painting, CreateUserForm, Like, Comment,avatar
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import PaintingUploadForm
from .forms import PaintingUpdateForm, avatar_user
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
# from .forms import PaintingSearchForm
def home(request):
    paintings = Painting.objects.all()
    return render(request,'pages/home.html',{'paintings':paintings})

def blog(request):
    paintings = Painting.objects.all()
    return render(request,'pages/blog.html',{'paintings':paintings})

def news(request):
    paintings = Painting.objects.all()
    return render(request,'pages/news.html',{'paintings':paintings})
    
def contact(request):
    paintings = Painting.objects.all()
    return render(request,'pages/contact.html',{'paintings':paintings})

def painting_list(request):
    paintings = Painting.objects.all()
    if request.user.is_authenticated:
        paintings_like = Like.objects.filter(user=request.user)
        return render(request,'pages/painting_list.html',{'paintings':paintings, "paintings_like": paintings_like})
    return render(request,'pages/painting_list.html',{'paintings':paintings})

@login_required
@user_passes_test(lambda a: a.is_staff)
def admin_list(request):
    paintings = Painting.objects.all()
    return render(request,'pages/admin_list.html',{'paintings':paintings})


def delete_pictures(request,pk):
    paintings = get_object_or_404(Painting,pk=pk)
    if request.method == 'POST':
        paintings.delete()
    return render(request,'pages/delete_pictures.html',{'paintings':paintings})


def edit_pictures(request,pk):
    painting = get_object_or_404(Painting,pk=pk)
    paintings = Painting.objects.all()
    return render(request,'pages/edit_pictures.html',{'painting':painting, 'paintings':paintings})

def update_pictures(request,pk):
    painting = get_object_or_404(Painting,pk=pk)
    form = PaintingUpdateForm(request.POST,instance=painting)
    if form.is_valid:
        form.save()
        messages.success(request,"Sửa thành công")
        return redirect('list')
    return render(request,'pages/edit_pictures.html',{ 'painting':painting})


def painting_detail(request,pk):
    painting = get_object_or_404(Painting,pk=pk)
    comments = reversed(Comment.objects.all())
    paintings = Painting.objects.all()
    if request.user.is_authenticated:
        is_user = request.user
        return render(request,'pages/paiting_detail.html',{'painting':painting, 'paintings':paintings, 'comments': comments, 'is_user': is_user})
    return render(request,'pages/paiting_detail.html',{'painting':painting, 'paintings':paintings, 'comments': comments})

@login_required
@user_passes_test(lambda u: u.is_staff)
def upload_painting(request):
    paintings = Painting.objects.all()
    if request.method == 'POST':
        form = PaintingUploadForm(request.POST,request.FILES) 
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = PaintingUploadForm()
    
    return render(request,'pages/upload.html',{'form':form,'paintings':paintings})

@login_required
def upload_avt(request):
    if request.method == 'POST':
        form = avatar_user(request.POST,request.FILES)
        if form.is_valid():
            avatars = avatar.objects.all()
            Avt = avatars.filter(user_painting = request.user)
            if not Avt:
                avatar_obj = form.save(commit=False)
                avatar_obj.user_painting = request.user
                avatar_obj.save()
            else:
               formUpdateAvt = avatar_user(request.POST,request.FILES, instance= Avt.first())
               if  formUpdateAvt.is_valid:
                   formUpdateAvt.save()
            return redirect('profile')
    else:
        form = avatar_user()
    return render (request,'pages/upload_Avt.html', {'form':form} )

# def painting_search(request):
#     form = PaintingSearchForm(request.GET)
#     if form.is_valid():
#         query = form.cleaned_data['query']
#         name = form.cleaned_data['name']
#         if name:
#             paintings = Painting.objects.filter(
#                 name__icontains=query,
#                 name=name
#             )
#         else:
#             paintings = Painting.objects.filter(
#                 name__icontains=query
#             )
#         return render(request, 'pages/painting_search.html', {'paintings': paintings})
#     else:
#         return render(request, 'pages/painting_search.html')
#     form = PaintingSearchForm(request.GET)
def painting_search(request):
    # form = PaintingSearchForm(request.GET)
    if 'query' in request.GET:
        query = request.GET.get('query')
        # paintings = Painting.objects.filter(name__icontains = query)
        multiple_query = Q(Q(name__icontains=query) | Q(upload_date__icontains=query))
        paintings = Painting.objects.filter(multiple_query)
        return render(request, 'pages/painting_search.html', {'paintings': paintings})
    else:
        paintings = Painting.objects.all()
        context = {
            'paintings': paintings 
        }
    return render(request, 'pages/painting_search.html',context)
        
def contact(request):
    return render(request, 'pages/contact.html')       

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginPage')
    context = {'form' : form}
    return render(request, 'pages/register.html', context)  

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password )
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'user or password not correct!')
    context = {}
    return render(request, 'pages/login.html', context)  

def logoutPage(request):
    logout(request)
    return redirect('loginPage')

def profile(request):
    painting_likes = Like.objects.filter(user=request.user)
    avatars = avatar.objects.filter(user_painting=request.user)
    return render(request, 'pages/profile_user.html', {'painting_likes':painting_likes, 'avatars' :  avatars})  

def like(request, pk):
    pain = get_object_or_404(Painting, pk=pk)
    like = Like(user=request.user, painting=pain)
    like.save()
    return redirect('list')

def like_delete(request, pk):
    pain = get_object_or_404(Painting, pk=pk)
    like = get_object_or_404(Like, user=request.user, painting=pain)
    like.delete()
    return redirect('list')
        
def add_comment(request, pk):
    try: 
        if(request.method == 'POST'):
            pain = get_object_or_404(Painting, pk=pk)
            #vì request.body trả về chuỗi dạng byte nên phải chuyển thành dạng utf8
            cmt_req = json.loads(request.body.decode('utf-8'))
            print(request.body)
            print(cmt_req)
            new_cmt = Comment(user=request.user, painting=pain, cmt=cmt_req.get('cmt'))
            new_cmt.save()
            res_data = {
                'username': request.user.username
            }
            res = {'messages': 'success', 'res_data': res_data}
            return JsonResponse(res)
    except Exception as e:  
         return JsonResponse({'message': 'error', 'error': str(e)})
