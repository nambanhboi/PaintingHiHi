from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse
from painting.models import Painting, PaintingLq, Comment
from .forms import PaintingUpdateForm, PaintingUploadForm
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.
def home(request):
    return HttpResponse("hihi")

@login_required
@user_passes_test(lambda a: a.is_staff)
def admin_list(request):
    paintings = Painting.objects.all()
    return render(request,'pages/admin_list.html',{'paintings':paintings})

@login_required
@user_passes_test(lambda u: u.is_staff)
def upload_painting(request):
    paintings = Painting.objects.all()
    if request.method == 'POST':
        form = PaintingUploadForm(request.POST, request.FILES)
        if form.is_valid():
            painting = form.save()  # Lưu ảnh gốc vào model Painting và nhận lại đối tượng đã lưu

            imagelqs = request.FILES.getlist('imagelq')  # Lấy danh sách các tệp tin ảnh liên quan từ trường 'imagelq'

            for imagelq in imagelqs:
                PaintingLq.objects.create(painting=painting, image=imagelq)  # Lưu từng ảnh liên quan với painting đã lưu

            return redirect('list')
    else:
        form = PaintingUploadForm()
    
    return render(request, 'pages/upload.html', {'form': form, 'paintings': paintings})
def edit_pictures(request,pk):
    painting = get_object_or_404(Painting,pk=pk)
    paintings = Painting.objects.all()
    paintinglq = PaintingLq.objects.filter(painting=painting)
    return render(request,'pages/edit_pictures.html',{'painting':painting, 'paintings':paintings, 'paintinglq': paintinglq})

def update_pictures(request,pk):
    painting = get_object_or_404(Painting,pk=pk)
    paintinglq = PaintingLq.objects.filter(painting=painting)
    form = PaintingUpdateForm(request.POST,instance=painting)
    if form.is_valid:
        form.save()
        messages.success(request,"Sửa thành công")
        return redirect('list')
    return render(request,'pages/edit_pictures.html',{ 'painting':painting, 'paintinglq': paintinglq})

def delete_pictures(request,pk):
    painting = get_object_or_404(Painting,pk=pk)
    comments = reversed(Comment.objects.all())
    paintings = Painting.objects.all()
    paintinglq = PaintingLq.objects.filter(painting=painting)
    if request.method == 'POST':
        painting.delete()
        return render(request,'pages/admin_list.html',{'painting':painting, 'paintings':paintings, 'comments': comments, 'paintinglq': paintinglq})
    else:
        return render(request,'pages/delete_pictures.html',{'painting':painting,'paintings':paintings, 'comments': comments, 'paintinglq': paintinglq})
