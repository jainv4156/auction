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
        return redirect("index")
    
    return render(request,"auctionlist.html")
def history(request):
    auctionhistoryitem=auctionitem.objects.all().filter(status="Sold")
    return renden(request,"itemmanager.html",{"objectlists":auctionhistory})
def deleteitem(request,p):
    data =auctionitem.objects.all().filter(itemid=p)
    data.delete()
    return redirect("auctionlist")

