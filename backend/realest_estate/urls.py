"""realest_estate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),    # API for the obtaining JWT token during login session.
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/accounts/', include('accounts.urls')),                                # API for the Account/User creation, SignUp Page
    path('api/realtors/', include('realtors.urls')),                                # API for the realtors page (Real Estate Agents) 
    path('api/listings/', include('listings.urls')),                                # API for the listings page (Listings posted by Agents) 
    path('api/contacts/', include('contacts.urls')),                                # API for the contacts page (Contacts posted by Users) 
    path('admin/', admin.site.urls),                                                # API for the admin page (Super User)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)                   # For accessing the media folder through the API

urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]  


