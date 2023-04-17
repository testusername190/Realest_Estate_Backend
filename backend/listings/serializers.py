from rest_framework import serializers
from .models import Listing


# Serailize specific fields for all the Listed property.
class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ('title', 'address', 'city', 'state', 'price', 'sale_type', 'home_type', 'bedrooms', 'bathrooms', 'sqft', 'photo_main', 'slug')


# Serailize all the fields for only a particular Listed Property.
class listingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'
        lookup_field = 'slug'       # Creating the correct URL for the Selected Listed Property.