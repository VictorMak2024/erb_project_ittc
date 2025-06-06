from django.contrib import admin
from django.forms import NumberInput
from django.db import models
from .models import Activity

# Register your models here.

class ActivityAdmin(admin.ModelAdmin):
    list_display = ('hotitem', 'title', 'name', 'date_start', 'date_end', 'time_start', 'time_end', 'location', 'medium', 'target', 'trainer', 'price', 'total_sit', 'onenquiry_sit', 'phaseOut', 'salesmen')
    list_display_links = ('title', 'name',)
    search_fields = ('title', 'name')
    list_editable = ('hotitem','medium', 'trainer', 'price', 'total_sit', 'onenquiry_sit','phaseOut')
    list_filter = ('hotitem', 'phaseOut')
    list_per_page = 25
    ordering = ['-id']
    formfield_overrides = {
        models.IntegerField: {'widget': NumberInput(attrs={'size' : '10'})},
    }

admin.site.register(Activity, ActivityAdmin)
