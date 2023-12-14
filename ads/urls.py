from django.urls import path
from .views import (
    AdCreateView, AdDetailView,
    #LocationListView, LocationDetailView,
    #VisitCountListView, VisitCountDetailView
)

urlpatterns = [
    path('ads/', AdCreateView.as_view(), name='ad-list'),
    path('ads/<int:pk>/', AdDetailView.as_view(), name='ad-detail'),
    #path('location/', LocationListView.as_view(), name='location-list'),
    #path('location/<int:pk>/', LocationDetailView.as_view(), name='location-detail'),
    #path('visitcounts/', VisitCountListView.as_view(), name='visitcount-list'),
    #path('visitcount/<int:pk>/', VisitCountDetailView.as_view(), name='visitcount-detail'),
]

