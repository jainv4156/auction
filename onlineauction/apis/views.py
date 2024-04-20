from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import auctionobjects
from .serializer import auctionitemSerializer,bidhistorySerializer
from .models import auctionitem, bidhistory
import django.utils.timezone as timezone
@api_view(['POST'])
def getData(request):
    if request.method == 'POST':
        data=request.data
        auction24item = auctionobjects.objects.all()[0]
        auctionitems=auctionitem.objects.all().filter(itemid=auction24item.itemid.itemid)
        serializer=auctionitemSerializer(auctionitems,many=True)
        itemhistory = bidhistory.objects.all().filter(itemid=auction24item.itemid.itemid).order_by('-bid')
        serializer2 = bidhistorySerializer(itemhistory,many=True)

        yourhighestbid=bidhistory.objects.all().filter(itemid=auction24item.itemid.itemid,bidder=data.get('user')).order_by('-bid')
        if(len(yourhighestbid)==0):
            return Response({"data2":serializer.data[0],"data":serializer2.data,"yourhighestbid":{"bid":0,"date":"None"}})
        else:            
            return Response({"data2":serializer.data[0],"data":serializer2.data,"yourhighestbid":{"bid":yourhighestbid[0].bid,"date":yourhighestbid[0].bidtime}})
    
@api_view(['POST'])
def bid(request):
    if request.method=='POST':
        data=request.data
        print(data.get('itemid'))
        print(data.get('bid'))
        print(data.get('bidder'))
        bidHistory=bidhistory.objects.create(itemid=data.get('itemid'),bid=data.get('bid'),bidtime=timezone.now(),bidder=data.get('bidder'))
        bidHistory.save()
        currentbider=auctionitem.objects.all().filter(itemid=data.get('itemid'))
        if len(currentbider)==0:
            return Response({"status":"failafsdf"})
        elif currentbider[0].currentbid<int(data.get('bid')):
            currentbider.update(currentbid=data.get('bid'),currentbidder=data.get('bidder'))
        return Response({"status":"success"})
        
@api_view(['GET'])
def results(request):
    if request.method == 'GET':
        auctionresutl=auctionitem.objects.all().filter(status="Sold")
        print(auctionresutl)
        serializer=auctionitemSerializer(auctionresutl,many=True)
        return Response(serializer.data)
