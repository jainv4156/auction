from django.shortcuts import render,redirect
from django.http import HttpResponse
from onedayauction.models import bidhistory,onedayitem
from django.contrib.auth.models import User
from datetime import datetime,time,date
# Create your views here.
def index(request):
    user=request.user
    if user.is_authenticated:
        bidinghistory= bidhistory.objects.all()
        itemhistory=onedayitem.objects.all()[0]
        if request.method=="POST":
            bid=request.POST.get("bid")
            user=request.user
            bidhistory.objects.create(bidder=user.username,bid=bid,bidtime=datetime.now(),itemid=itemhistory.itemid,itemname=itemhistory.itemname)
            itemhistory.currentbid=bid
            itemhistory.currentbidder=user.username
            itemhistory.save()
            return redirect("index")
        else:
            return render(request,"onedayauction.html",{'bidhistories':bidinghistory,'itemhistories':itemhistory,'timeleft':datetime.now().strftime("%H:%M:%S")})
    else:
        return render(request,"firstpage.html")
