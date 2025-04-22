from django.urls import path
from . import views

# Create your views here.

urlpatterns = [
    path('activity_contact', views.activity_contact, name='activity_contact'),
    path('course_contact', views.course_contact, name='course_contact'),
<<<<<<< HEAD
    path('product_contact', views.product_contact, name='product_contact'), # add this line to path('contact', views.contact, name='contact'), # add this line to the urlpattens for the contacts
    path('takeOrder', views.takeOrder, name='takeOrder'),
    # add this line to path('contact', views.contact, name='contact'), # add this line to the urlpattens for the contacts
    path('delete_takeOrder<int:takeOrder_id>', views.delete_takeOrder, name='delete_takeOrder'),
    path('delete_take<int:takeOrder_id>', views.delete_take, name='delete_take'),
=======
    path('porduct_contact', views.product_contact, name='product_contact'), # add this line to path('contact', views.contact, name='contact'), # add this line to the urlpattens for the contacts
#    path('<int:contact_id>', views.delete_contact, name='delete_contact'),
>>>>>>> origin/WCNgApps
]