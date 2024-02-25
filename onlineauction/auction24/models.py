from django.db import models

# Create your models here.
class auctionobjects(models.Model):
    slot = models.IntegerField(primary_key=True)
    itemid   = models.ForeignKey("onedayauction.auctionitem", on_delete=models.CASCADE)
    