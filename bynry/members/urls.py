from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('newrequest/', views.newrequest, name='newrequest'),
    path('viewrequest/', views.viewrequest, name='viewrequest'),
]