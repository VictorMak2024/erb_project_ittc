from django.contrib import admin
from .models import ShoppingCart
from contacts.models import TakeOrder

# Register your models here.
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'total_Amount', 'is_paid', 'is_shipped', 'is_completed', 'created_at')
    list_display_links = ('id', 'user_id')
    search_fields = ('user_id', 'ship_date')
    list_per_page = 25

def get_orders(self, obj):
        return ", ".join([f"{order.product.no} (Qty: {order.onOrderQty})" for order in obj.orders.all()])
get_orders.short_description = 'Orders'

admin.site.register(ShoppingCart, ShoppingCartAdmin)