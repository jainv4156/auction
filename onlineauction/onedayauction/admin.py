from django.contrib import admin
from .models import bidhistory
from.models import auctionitem

# Register your models here.
admin.site.register(bidhistory)
admin.site.register(auctionitem)
