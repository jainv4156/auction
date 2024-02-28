from django.db import models

# Create your models here.

class bidhistory(models.Model):
    id = models.AutoField(primary_key=True)
    itemid = models.IntegerField()
    # itemname = models.CharField(max_length=100)
    bid = models.IntegerField()
    bidtime = models.DateTimeField()
    bidder = models.CharField(max_length=100)
    
class auctionitem(models.Model):
    itemid = models.IntegerField(primary_key=True)
    itemname = models.CharField(max_length=100)
    itemdiscription = models.CharField(max_length=100)
    itemstartingprice = models.IntegerField()
    itemimage = models.ImageField(upload_to='images/',default="images/sitar.jpg")
    currentbidder = models.CharField(max_length=100,default="None")
    status = models.CharField(max_length=100,default="NotSold")
    currentbid=models.IntegerField(default=0)
    slots = models.IntegerField(null=True, blank=True)
    listdate = models.DateTimeField( null=True, blank=True)
    