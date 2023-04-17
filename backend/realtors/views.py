from django.shortcuts import render
from .serializers import RealtorSerializer
from .models import Realtor
from rest_framework import permissions
from rest_framework.generics import ListAPIView,RetrieveAPIView 
import logging

logger = logging.getLogger("django")

# ListAPIView used to get all the objects from the database for the Realtors tables.                    Only GET method works here
# RetrieveAPIView used to get a particular object filtered by its primary key from the Realtors table.  Only GET method works here

# Create your views here.

class RealtorListView(ListAPIView):
    logger.info("\n Inside the RealtorListView API of realtor App. Here we are getting all the realtors from DB..")

    permission_classes = (permissions.AllowAny, )       # By default we will be authenticated before accessing this view, hence we don't need to check for authentication here.
    queryset = Realtor.objects.all()                    # Access all the Realtors from the table.
    serializer_class = RealtorSerializer                # Serialize it to a JSON format and for sending it to the frontend.
    pagination_class = None

class RealtorView(RetrieveAPIView):
    logger.info("\n Inside the RealtorView API of realtor App. Here we are a particular realtors from DB based on its PK..")

    queryset = Realtor.objects.all()                    # Retreive the particular object filtered by the primary key
    serializer_class = RealtorSerializer                # Serialize it to a JSON format and for sending it to the frontend.

class TopSellerView(ListAPIView):     
    logger.info("\n Inside the TopSellerView API of realtor App. Here we are getting all the realtors who are topsellers..")

    permission_classes = (permissions.AllowAny, )
    queryset = Realtor.objects.filter(top_seller=True)  # Retreive only those object who have the feild top_seller as true.
    serializer_class = RealtorSerializer                # Serialize it to a JSON format and for sending it to the frontend.
    pagination_class = None                             # It will have a list but it will be single object.