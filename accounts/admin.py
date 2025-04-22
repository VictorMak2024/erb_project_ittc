from django.contrib import admin
from .models import ShoppingCart

# Register your models here.
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('id','user_id', 'ship_date','is_paid', 'created_at')
    list_display_links = ('id', 'user_id')
    search_fields = ('ship_date',)
    list_per_page = 25

admin.site.register(ShoppingCart, ShoppingCartAdmin)