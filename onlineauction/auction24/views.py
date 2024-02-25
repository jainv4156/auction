from django.shortcuts import render
from .models import auctionobjects
from  auction24.task import add,time_update
# Create your views here.
def auction24(request):
    auction24item = auctionobjects.objects.all()
    context={'auction24':auction24item}
    result = time_update.delay()
    print(result)
    return render(request,"auction24.html",context)


