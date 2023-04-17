from django.urls import path
from .views import RealtorListView, RealtorView, TopSellerView

# Here we are defining our views for the creation of a user. 
# 
# The url will be localhost:8000/api/realtors/  --> call the all the realtors using RealtorListView
# The url will be localhost:8000/api/realtors/1  --> call the all the realtor with primary key 1 using RealtorView
# The url will be localhost:8000/api/realtors/topseller  --> call the all the realtors with topseller field as true using TopSellerView

urlpatterns = [
    path('', RealtorListView.as_view()),
    path('topseller', TopSellerView.as_view()),
    path('<pk>', RealtorView.as_view()),
]