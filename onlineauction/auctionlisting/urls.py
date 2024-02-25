from django.urls import path
from auctionlisting import views
urlpatterns = [ 
    path('',views.auctionlist,name="auctionlist"),
    path('additem/',views.additem,name="additem"),
    path('history/',views.history,name="history"),
    path('deleteitem/<str:p>',views.deleteitem,name="deleteitem"),
    path('updateitem/<str:p>',views.updateitem,name="updateitem"),
]