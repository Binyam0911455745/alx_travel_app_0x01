from rest_framework import serializers
from .models import Listing, Booking, Review

class ListingSerializer(serializers.ModelSerializer):
    """
    Serializer for the Listing model.
    """
    amenities = serializers.SerializerMethodField()

    class Meta:
        model = Listing
        fields = [
            'id', 'title', 'description', 'address', 'city', 'country',
            'price_per_night', 'max_guests', 'bedrooms', 'bathrooms',
            'amenities', 'is_active', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']

    def get_amenities(self, obj):
        """
        Converts the comma-separated amenities string into a list of strings.
        """
        if obj.amenities:
            return [amenity.strip() for amenity in obj.amenities.split(',')]
        return []

    def to_internal_value(self, data):
        """
        Converts the list of amenities back to a comma-separated string for saving.
        """
        if 'amenities' in data and isinstance(data['amenities'], list):
            data['amenities'] = ','.join(data['amenities'])
        return super().to_internal_value(data)

class BookingSerializer(serializers.ModelSerializer):
    """
    Serializer for the Booking model.
    Includes read-only fields for listing title and guest username.
    """
    listing_title = serializers.ReadOnlyField(source='listing.title')
    guest_username = serializers.ReadOnlyField(source='guest.username')
    status_display = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = Booking
        fields = [
            'id', 'listing', 'listing_title', 'guest', 'guest_username',
            'check_in_date', 'check_out_date', 'total_price', 'status',
            'status_display', 'created_at', 'updated_at'
        ]
        read_only_fields = ['total_price', 'status', 'created_at', 'updated_at']

    def validate(self, data):
        """
        Check that the check_in_date is before the check_out_date.
        """
        if data['check_in_date'] >= data['check_out_date']:
            raise serializers.ValidationError("Check-out date must be after check-in date.")
        return data

class ReviewSerializer(serializers.ModelSerializer):
    """
    Serializer for the Review model.
    """
    listing_title = serializers.ReadOnlyField(source='booking.listing.title')
    guest_username = serializers.ReadOnlyField(source='guest.username')
    booking_id = serializers.ReadOnlyField(source='booking.id')

    class Meta:
        model = Review
        fields = [
            'id', 'booking', 'booking_id', 'guest', 'guest_username',
            'listing_title', 'rating', 'comment', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at', 'guest', 'booking']
