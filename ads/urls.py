from django.urls import path
from .views import (
    AdCreateView, AdDetailView,
    LocationCreateView, LocationDetailView,
    #VisitCountListView, VisitCountDetailView
)

urlpatterns = [
    path('ad/', AdCreateView.as_view(), name='ad-list'),
    path('ad/<int:pk>/', AdDetailView.as_view(), name='ad-detail'),
    path('location/', LocationCreateView.as_view(), name='location-list'),
    path('location/<int:pk>/', LocationDetailView.as_view(), name='location-detail'),
    #path('visitcounts/', VisitCountListView.as_view(), name='visitcount-list'),
    #path('visitcount/<int:pk>/', VisitCountDetailView.as_view(), name='visitcount-detail'),
]

