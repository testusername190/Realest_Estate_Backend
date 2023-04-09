from django.urls import path
from .views import SignupView

#Here we are defining our views for the creation of a user. The url will be localhost:8000/api/accounts/signup


urlpatterns = [
    path('signup', SignupView.as_view()),
]