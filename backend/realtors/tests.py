from django.test import TestCase, Client
from django.urls import reverse
from .models import Realtor


# Create your tests here.

class TestRealtorsModels(TestCase):
    def setUp(self):
        Realtor.objects.create(
            name='Test Realtor',
            phone='555-555-5555',
            email='testrealtor@example.com',
            top_seller=True,
            )
    def test_realtor_model(self):
        realtor = Realtor.objects.get(name='Test Realtor')
        self.assertEqual(realtor.phone, '555-555-5555')
        self.assertEqual(realtor.email, 'testrealtor@example.com')
        self.assertTrue(realtor.top_seller)

        
# python3 manage.py test realtors.tests
            




