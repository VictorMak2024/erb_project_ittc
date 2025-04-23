from django.contrib import admin

# Register your models here.
from django.forms import NumberInput
from django.db import models 
from .models import SupportResource

class SupportResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'photo', 'description', 'web_url', 'list_date','sr_items')
    list_filter = 'sr_items',
    list_display_links = 'title',
    search_fields = ('title','sr_items__itemsname')
    list_editable = 'description','web_url','sr_items',
    list_per_page = 25

admin.site.register(SupportResource, SupportResourceAdmin)
