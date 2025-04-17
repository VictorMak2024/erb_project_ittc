from django.contrib import admin
from .models import Contactmessage
from django.utils.html import format_html

#Register your models here

class ContactmessageAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'email', 'phone', 'post_date', 'center', 'user_id', 'message'
    
    list_display_links = 'id', 'name'
    # readonly_fields = 'user_id'
    search_fields = 'name', 'email', 'center', 'post_date', 'phone'
    list_per_page = 25

admin.site.register(Contactmessage, ContactmessageAdmin)
# Register your models here.
