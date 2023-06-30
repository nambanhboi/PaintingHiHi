from django.urls import path
from . import views
urlpatterns = [
    path('register/',views.register,name='register'),
    path('loginPage/',views.loginPage,name='loginPage'),
    path('logoutPage/',views.logoutPage,name='logoutPage'),
    path('', views.home,name='home'),
    path('explore/', views.painting_list,name='list'),
    path('detail/<int:pk>/',views.painting_detail,name='detail'),
    path('search/',views.painting_search,name='search'),
    path('blog/',views.blog,name='blog'),
    path('news/',views.news,name='news'),
    path('contact/',views.contact,name='contact'),
    path('profile/', views.profile, name='profile'),
    path('like/<int:pk>/', views.like, name='like'),
    path('like_delete/<int:pk>/', views.like_delete, name='like_delete'),
    path('add_comment/<int:pk>/', views.add_comment, name='add_comment'),
    path('upload_avt/', views.upload_avt, name='upload_avt'),
]
