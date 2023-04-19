from django.test import TestCase, Client
from django.urls import reverse
from .models import Listing
from realtors.models import Realtor

# Create your tests here.

class TestListings(TestCase):
    def setUp(self):
        self.realtor = Realtor.objects.create(
            name='Test Realtor',
            phone='555-555-5555',
            email='testrealtor@example.com',
            top_seller=True,
        )

        Listing.objects.create(
            title = 'Mera Ghar',
            address = '433, Jadav Ghosh Road',
            city = 'Kolkata',
            state = 'West Bengal',
            description = 'A 3 storey house in Behala Sarsuna Kolkata about 3 km from metro station',
            sale_type = 'For Sale',
            price = 10000000,
            bedrooms = 5,
            bathrooms = 5.0,
            home_type = 'House',
            sqft  = 1000,
            realtor = self.realtor
            )
        
    def test_listings_model(self):
        listing = Listing.objects.get(title='Mera Ghar')
        self.assertEqual(listing.address, '433, Jadav Ghosh Road')
        self.assertEqual(listing.city, 'Kolkata')
        self.assertEqual(listing.state, 'West Bengal')
        self.assertNotEqual(listing.description, '433, Jadav Ghosh Road')
        self.assertEqual(listing.price, 10000000)
        self.assertEqual(listing.bedrooms, 5)
        self.assertEqual(listing.sqft, 1000)
        self.assertEqual(listing.address, '433, Jadav Ghosh Road')


        
# python3 manage.py test listings.tests