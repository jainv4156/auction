from django.shortcuts import render,redirect
from onedayauction.models import auctionitem

# Create your views here.
def auctionlist(request):   
    objectlist=auctionitem.objects.all().filter(status="NotSold")
    context={"objectlists":objectlist}
    return render(request,"itemmanager.html",context)
def additem(request):   
    if request.method == "POST":
        itemid = request.POST.get("item_id")
        itemname = request.POST.get("item_name")
        itemdiscription = request.POST.get("description")
        itemstartingprice = request.POST.get("starting_price")
        # itemimage = request.FILES["image"]
        # itemauctiondate = request.POST.get("auction_date")
        data=auctionitem(itemid=itemid,itemname=itemname,itemdiscription=itemdiscription,itemstartingprice=itemstartingprice)
        data.save() 
        return redirect("auction24")
    
    return render(request,"auctionlist.html")
def history(request):
    auctionhistoryitem=auctionitem.objects.all().filter(status="auctioned/sold")
    return render(request,"itemmanager.html",{"objectlists":auctionhistoryitem})
def deleteitem(request,p):
    data =auctionitem.objects.all().filter(itemid=p)
    data.delete()
    return redirect("auctionlist")
def updateitem(request,p):
    data =auctionitem.objects.get(itemid=p)
    if request.method == "POST":
        itemid = request.POST.get("item_id")
        itemname = request.POST.get("item_name")
        itemdiscriptions = request.POST.get("description")
        itemstartingprice = request.POST.get("starting_price")
        data.itemid=itemid
        data.itemname=itemname
        descrip=data.itemdiscription
        if itemdiscription != "":
            data.itemdiscription=itemdiscriptions
        data.itemdiscription=descrip
        data.itemstartingprice=itemstartingprice
        data.save()
        return redirect("auctionlist")
    return render(request,"itemupdate.html",{"data":data})

