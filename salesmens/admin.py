from django.contrib import admin
#from datetime import datetime
# Register your models here.
from .models import Salesmen

# add this class for the admin page to display the realtors
class SalesmenAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_mvp', 'name', 'email', 'hire_date')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_editable = ('is_mvp',)
    list_per_page = 25

admin.site.register(Salesmen, SalesmenAdmin)