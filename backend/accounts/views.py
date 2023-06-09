from django.contrib.auth import get_user_model
User = get_user_model()

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
import logging

logger = logging.getLogger("django")


#The class SignUpView is a API View to handle the POST request for the creation of the new users.
#Logic used here is: provided 2 password should be equal email should be unique and length of the password should be >6.
#If all the logic matches then we create the user by calling the create_user in the models.py file else throw an error back to the frontend.

#We have created a view to signup the new user here, but for login for an existing user we will not be creating a separate view instead we will
# handle it using JWT authentication.

class SignupView(APIView):
    logger.info("\n Inside the SignupView API of accounts APP. Here we are creating an account of a user. JWT token not needed. ")

    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data

        name = data['name']
        email = data['email']
        password = data['password']
        password2 = data['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():

                logger.error("\n Inside the post function of SignupView API of accounts APP. Passwords have matched but the email already exists. ")                
                return Response({'error': 'Email already exists'})
            
            else:
                if len(password) < 6:

                    logger.error("\n Inside the post function of SignupView API of accounts APP. Passwords length < 6. ")
                    return Response({'error': 'Password must be at least 6 characters'})
                
                else:
                    user = User.objects.create_user(email=email, password=password, name=name)
                    user.save()

                    logger.info("\n User creation successfull!! ")
                    return Response({'success': 'User created successfully'})
        else:

            logger.error("\n Inside the post function of SignupView API of accounts APP. Entered Passwords didnot match.")
            return Response({'error': 'Passwords do not match'})