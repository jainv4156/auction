from django.shortcuts import render
from .models import auctionobjects

# Create your views here.
def auction24(request):
    auction24item = auctionobjects.objects.all()
    context={'auction24':auction24item}
    return render(request,"auction24.html",context)

