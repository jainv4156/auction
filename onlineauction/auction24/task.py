from celery import shared_task
from time import sleep
from onedayauction.models import auctionitem
from datetime import datetime
from auction24.models import auctionobjects
@shared_task
def add(x, y):
    sleep(5)
    return x + y

@shared_task
def time_update():
    if auctionitem.objects.all().filter(status="NotSold").count()==0:
        return "done"
    auctioning_item=auctionitem.objects.all().filter(status="auctioning")
    for i in auctioning_item:
        i.slots+=1
        if i.slots==13:
            i.status="auctioned/sold"
            i.slots=0
        i.save()


    new_item=auctionitem.objects.all().filter(status="NotSold")[0]
    print(new_item.itemid)
    new_item.status="auctioning"
    new_item.slots=1
    new_item.listdate=datetime.now()
    new_item.save()

    #seting up slots for auctioning items
    slots_=auctionobjects.objects.all()
    for i in slots_:
        slotobjectid=auctionitem.objects.get(slots=i.slot)
        i.itemid=slotobjectid
        i.save()
    return "done"

