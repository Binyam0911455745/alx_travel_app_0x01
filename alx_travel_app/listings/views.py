# alx_travel_app_0x01/listings/views.py

from rest_framework import viewsets, permissions
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer

# --- Listing ViewSet ---
class ListingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows listings to be viewed, created, updated or deleted.
    """
    queryset = Listing.objects.all().order_by('title') # Order as desired
    serializer_class = ListingSerializer
    # Permissions:
    # IsAuthenticatedOrReadOnly allows GET, HEAD, OPTIONS for unauthenticated users,
    # but requires authentication for POST, PUT, PATCH, DELETE.
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # You might add custom logic here, e.g., to filter listings by owner for write operations
    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user) # If Listing has an 'owner' field

# --- Booking ViewSet ---
class BookingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows bookings to be viewed, created, updated or deleted.
    """
    queryset = Booking.objects.all().order_by('-check_in_date') # Order as desired
    serializer_class = BookingSerializer
    # Permissions for bookings are usually stricter: only authenticated users can book.
    # Often, a user can only view/manage their own bookings.
    permission_classes = [permissions.IsAuthenticated]

    # Example: Filter bookings to only show current user's bookings (for list and retrieve)
    def get_queryset(self):
        # If the user is an admin, they can see all bookings
        if self.request.user.is_staff:
            return Booking.objects.all()
        # Otherwise, only show bookings where they are the guest
        return Booking.objects.filter(guest=self.request.user).order_by('-start_date')

    # Example: Automatically set the guest for new bookings to the current user
    def perform_create(self, serializer):
        serializer.save(guest=self.request.user)