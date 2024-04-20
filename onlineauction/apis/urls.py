from django.urls import path,include
from . import views
urlpatterns = [
    path('data/',views.getData,name="getData"),
    path('bid/',views.bid,name="bid"),
    path('results/',views.results,name="results"),
    # path('bidinghistory',views.bidinghistory,name="bidinghistory"),
]