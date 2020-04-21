
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path("", views.index,name='index'),
    path("wvideos/", views.wvideos,name='WebVideos'),
    path("channels/", views.channels,name='channels'),
    path("category/", views.category,name='category'),
    path("stars/", views.stars,name='stars'),
    path("", views.index,name='WebVideos'),
    
    
    
]
