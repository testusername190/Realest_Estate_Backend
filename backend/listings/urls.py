from django.urls import path
from .views import ListingsView, ListingView, SearchView

# Declare the URL for the listings app here.

urlpatterns = [
    path('', ListingsView.as_view(),name="ListALL"),           
    path('search', SearchView.as_view()),
    path('<slug>', ListingView.as_view()),      # Used for lising a particular view, not by PK(id) but by Slug field.
]