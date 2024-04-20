from django.contrib import admin
from .models import auctionitem,bidhistory,auctionobjects
# Register your models here.
admin.site.register(auctionitem)
admin.site.register(bidhistory)
admin.site.register(auctionobjects)