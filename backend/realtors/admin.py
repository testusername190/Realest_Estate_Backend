from django.contrib import admin
from .models import Realtor


# Register your model here.


class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'date_hired')        # Fields to be displayed in the admin section.
    list_display_links = ('id', 'name')                         # Clickable links in the admin section.
    search_fields = ('name', )                                  # Search option based on name in the admin section.
    list_per_page = 25                                          # Simple pagination with 25 display per page.

admin.site.register(Realtor, RealtorAdmin)                      # Registering the model Realtor here.