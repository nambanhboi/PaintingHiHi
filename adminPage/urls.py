from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="homeAdmin"),
    path('upload/', views.upload_painting, name="upload_painting"),
    path('admin_list/',views.admin_list,name='admin_list'),
    path('edit_pictures/<int:pk>/',views.edit_pictures,name='edit_pictures'),
    path('update_pictures/<int:pk>/',views.update_pictures,name='update_pictures'),
    path('delete_pictures/<int:pk>/',views.delete_pictures,name='delete_pictures'),
]