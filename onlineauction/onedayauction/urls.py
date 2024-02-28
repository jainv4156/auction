from django.contrib import admin
from django.urls import path, include # new
from . import views
urlpatterns = [
    path('onedayauction/<str:pk>/',views.index,name="index"),
    
]
