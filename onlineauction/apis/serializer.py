from rest_framework import serializers
from .models import auctionobjects
from .models import auctionitem, bidhistory
class auction24Serializer(serializers.ModelSerializer):
    class Meta:
        model = auctionobjects
        fields = '__all__'  
        
class auctionitemSerializer(serializers.ModelSerializer):
    class Meta:
        model = auctionitem
        fields = '__all__'

class bidhistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = bidhistory
        fields = '__all__'