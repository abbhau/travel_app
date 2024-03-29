from django.urls import path
from .views import (DestinationCreate, DestinationList, DestinationDetailView,
                    DestinationUpdateView, DestinationDeleteView)

urlpatterns = [
    path('destinations/', DestinationList.as_view(), name='destination-list'),
    path('destinations/create/', DestinationCreate.as_view(), name='destination-create'),
    path('destinations/<int:pk>/', DestinationDetailView.as_view(), name='destination-detail'),
    path('destinations/update/<int:pk>/', DestinationUpdateView.as_view(), name='destination-update'),
    path('destinations/delete/<int:pk>/', DestinationDeleteView.as_view(), name='destination-delete'),
]