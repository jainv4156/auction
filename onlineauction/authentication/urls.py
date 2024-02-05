from django.contrib import admin
from django.urls import path, include # new
from authentication import views
urlpatterns = [
    path('',views.fisrstpage,name="firstpage"),
    path('signup_user', views.signup_user,name="signup_user"),  
    path('login_user', views.login_user,name="login_user"),  
    path('logout_user', views.logout_user,name="logout_user"),
]