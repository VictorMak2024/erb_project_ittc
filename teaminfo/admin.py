from django.contrib import admin


# Register your models here.
# from django.forms import NumberInput
from django.db import models 
# Register your models here.

from .models import Teams

 
class TeaminfoAdmin(admin.ModelAdmin):

    list_display=('id','name','position','duty','detail')
    list_editable='name','position','duty','detail'
    ordering = '-id',

    # formfield_overrides = {
    #     models.IntegerField: {'widget': NumberInput(attrs={'type': 'number'})},
    # }

admin.site.register(Teams,TeaminfoAdmin)