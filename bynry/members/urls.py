from django.urls import path
from . import views
from django.urls.conf import include  
from django.conf import settings  
from django.conf.urls.static import static  

urlpatterns = [
    path('', views.home, name='home'),
    path('newrequest/', views.newrequest, name='newrequest'),
    path('viewrequest/', views.viewrequest, name='viewrequest'),
]

if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  

