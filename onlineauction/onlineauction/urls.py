
from django.contrib import admin
from django.urls import path, include # new
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("onedayauction.urls")),
    path('',include("authentication.urls")),
    path('',include("auction24.urls")),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
