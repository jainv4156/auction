from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def fisrstpage(request):
    user=request.user
    if user.is_authenticated:
        return redirect("auction24")
    return render(request,"firstpage.html")
def signup_user(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        email=request.POST.get("email")
        firstname=request.POST.get("firstName")
        lastname=request.POST.get("lastName")
        
        user=User.objects.create_user(username=username,password=password,email=email,first_name=firstname,last_name=lastname)
        user.save()
        user=authenticate(username=username,password=password)
        login(request,user) 
        return redirect("auction24")
    else :


        return render(request,"signup_userdetailform.html")
def login_user(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(username=username,password=password)
        
        if user is not None :
            login(request,user)
            return redirect("auction24")
        else:
            return render(request,"signup_userdetailform.html")
    else:
        return render(request,"login_user.html")

def logout_user(request):
    logout(request)
    return redirect("firstpage")