from django.urls import path
from . import views

urlpatterns = [
    path('', views.file_upload, name='file_upload'),
    path('delete/<pk>', views.file_delete, name='file_delete'),
]