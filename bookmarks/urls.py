from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('edit/<str:pk>', views.BookmarkUpdate.as_view(), name='edit'),
    path('read/<str:pk>', views.read, name='read'),
    path('delete/<str:pk>', views.delete, name='delete')
]