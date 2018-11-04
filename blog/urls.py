from django.urls import path, include

from . import views 

urlpatterns = [
    path('', views.index, name='blog'),
    path('post/<int:pk>/', views.post, name='post'),
]