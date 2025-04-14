from django.contrib import admin
from django.forms import NumberInput
from django.db import models
from .models import Product, Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'photos')
    display_links = ('title', 'description', 'photos')
    editable = ('description',)
    

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('hotitem','title', 'no', 'price', 'stockQty', 'onOrderQty', 'phaseOut','photo_main')
    list_display_links = ('title',)
    search_fields = ('title', 'name')
    list_editable = ('hotitem', 'price', 'stockQty', 'onOrderQty', 'phaseOut')
    list_filter = ('hotitem', 'phaseOut')
    list_per_page = 25
    ordering = ['-id']
    formfield_overrides = {
        models.IntegerField: {'widget': NumberInput(attrs={'size' : '10'})},
    }

admin.site.register(Product, ProductAdmin)