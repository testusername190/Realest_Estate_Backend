from django.test import TestCase, Client
from django.urls import reverse
from .models import Contact

# Create your tests here.

class TestContactsModel(TestCase):
    def setUp(self):
        Contact.objects.create(
            name= 'Test User',
            email= 'testuser@example.com',
            subject =  'This is a test query',
            message = 'Yo Yo!! Whats Up Dude??'
        )
    def test_Contacts_model(self):
        contact = Contact.objects.get(name= 'Test User')
        self.assertEqual(contact.email , 'testuser@example.com')
        self.assertNotEqual(contact.subject, 'dskjfbdsf')
        self.assertEqual(contact.message , 'Yo Yo!! Whats Up Dude??')

#command to exeute the test script : python3 manage.py test contacts.tests