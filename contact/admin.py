from django.contrib import admin
from .models import Contact

#Register your models here

class ContactAdmin(admin.ModelAdmin):
    list_display = 'contact_id', 'center', 'email', 'phone', 'fax', 'address', 'office_hours', 'website'
    list_display_links = 'contact_id', 'center'
    
    # readonly_fields = 'user_id', 'contact_id'
    # search_fields = 'name', 'email', 'title', 'company'
    list_per_page = 25

admin.site.register(Contact, ContactAdmin)

# Register your models here.
