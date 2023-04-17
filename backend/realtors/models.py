from django.db import models
from datetime import datetime


#define your model Realtor here..

class Realtor(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')     #the uploaded pictures will be present in the photos folder in backend dir. with current year and current month as the sub dir. followed by current day as another sub dir.
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    top_seller = models.BooleanField(default=False)
    date_hired = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name