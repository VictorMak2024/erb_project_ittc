from django.contrib import admin

# Register your models here.
from django.forms import NumberInput
from django.db import models 
# Register your models here.

from .models import Jobs 
class JobsAdmin(admin.ModelAdmin):

    list_display=('id','title','job_type','salary','post_date','responsibilities','requirement','location','company','logo_url','email')
    list_editable='responsibilities','requirement','location'
    search_fields = 'title','description','location','responsibilities','requirement','company','job_type'
    
    ordering = '-id',

    formfield_overrides = {
        models.IntegerField: {'widget': NumberInput(attrs={'type': 'number'})},
    }

admin.site.register(Jobs,JobsAdmin)