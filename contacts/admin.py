from django.contrib import admin
<<<<<<< HEAD
from .models import Activity_Contact, Course_Contact, Product_Contact, TakeOrder
=======
from .models import Activity_Contact, Course_Contact, Product_Contact
>>>>>>> origin/WCNgApps

# Register your models here.
class Activity_ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'contact_date', 'activity_id')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'activity_id')
    list_per_page = 25

admin.site.register(Activity_Contact, Activity_ContactAdmin)

class Course_ContactAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ('id', 'name', 'email', 'phone', 'contact_date', 'course_id', 'course_id')
=======
    list_display = ('id', 'name', 'email', 'phone', 'contact_date', 'course_id')
>>>>>>> origin/WCNgApps
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'course_id')
    list_per_page = 25

admin.site.register(Course_Contact, Course_ContactAdmin)

class Product_ContactAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ('id', 'product', 'name', 'email', 'phone', 'contact_date', 'product_id')
=======
    list_display = ('id', 'name', 'email', 'phone', 'contact_date', 'product_id')
>>>>>>> origin/WCNgApps
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'product_id')
    list_per_page = 25

admin.site.register(Product_Contact, Product_ContactAdmin)
<<<<<<< HEAD

class TakeOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'price','onOrderQty', 'contact_date')
    list_display_links = ('id', 'product')
    #search_fields = ('product')
    list_per_page = 25

admin.site.register(TakeOrder, TakeOrderAdmin)
=======
>>>>>>> origin/WCNgApps
