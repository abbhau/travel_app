from django.urls import path
from .views import DestinationCreate, DestinationList

urlpatterns = [
    path('destinations/', DestinationList.as_view(), name='destination-list'),
    path('destinations/create/', DestinationCreate.as_view(), name='destination-create'),
]