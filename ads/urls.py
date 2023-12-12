from django.urls import path
from .views import AdvertisementView

urlpatterns = [
    path('ads/', AdvertisementView.as_view(), name='ads'),
]