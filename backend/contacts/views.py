from rest_framework import permissions
from rest_framework.views import APIView
from .models import Contact
from django.core.mail import send_mail
from rest_framework.response import Response

# Creating the view for the Contact App

class ContactCreateView(APIView):
    permission_classes = (permissions.AllowAny, )        # Login not mandatory..

    # Here we will take a JSON data from a FORM from the frontend and use it send an email to a respective user.
    def post(self, request, format=None):
        data = self.request.data

        # All the input subject, name, emailId, message will be passed through the FORM in the frontend..
        try:
            send_mail(
                data['subject'],
                'Name: '
                + data['name']
                + '\nEmail: '
                + data['email']          # Recipient Email ID.
                + '\n\nMessage:\n'
                + data['message'],
                'testusername190@gmail.com',                # Sender Email Id
                ['testusername190@gmail.com','sbrc1996@gmail.com','rvishal251996@gmail.com'],           # Admin Email Id to oversee the message
                fail_silently=False
            )

            contact = Contact(name=data['name'], email=data['email'], subject=data['subject'], message=data['message'])
            contact.save()

            return Response({'success': 'Message sent successfully'})

        except:
            return Response({'error': 'Message failed to send'})