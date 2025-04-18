# Register your models here.
from django.contrib import admin

# Register your models here.
# from django.forms import NumberInput
from django.db import models 
# Register your models here.

from .models import Newsevents
class NewseventsAdmin(admin.ModelAdmin):

    list_display=('id','title','post_date','is_News','is_Events','location','image','detail','iframe')
    list_editable='title','detail','location','image','post_date','is_News','is_Events','iframe'
    search_fields = 'title','location','detail','post_date','is_News','is_Events'
    
    ordering = '-id',

    # formfield_overrides = {
    #     models.IntegerField: {'widget': NumberInput(attrs={'type': 'number'})},
    # }

admin.site.register(Newsevents,NewseventsAdmin)