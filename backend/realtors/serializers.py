# Define your serializers here.
# Serializer helps us to convert the python object into a JSON format and send it to the frontend for display.

from rest_framework import serializers
from .models import Realtor

class RealtorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realtor
        fields = '__all__'

