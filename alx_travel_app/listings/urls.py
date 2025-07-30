# alx_travel_app_0x01/listings/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ListingViewSet, BookingViewSet # Import your ViewSets

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'listings', ListingViewSet) # This will create URLs like /listings/, /listings/{id}/
router.register(r'bookings', BookingViewSet) # This will create URLs like /bookings/, /bookings/{id}/

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]