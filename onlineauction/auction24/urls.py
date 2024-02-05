from django.urls import path, include # new
from auction24 import views
urlpatterns = [
    path('auction24',views.auction24,name="auction24"),
    ]
