from django.urls import path
from auctionlisting import views
urlpatterns = [ 
    path('',views.auctionlist,name="auctionlist"),
    path('additem/',views.additem,name="additem"),
]