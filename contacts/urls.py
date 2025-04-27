from django.urls import path
from . import views

# Create your views here.

urlpatterns = [
    path('activity_contact', views.activity_contact, name='activity_contact'),
    path('course_contact', views.course_contact, name='course_contact'),
    path('product_contact', views.product_contact, name='product_contact'), # add this line to path('contact', views.contact, name='contact'), # add this line to the urlpattens for the contacts
    path('takeOrder', views.takeOrder, name='takeOrder'),
    # add this line to path('contact', views.contact, name='contact'), # add this line to the urlpattens for the contacts
    path('delete_takeOrder<int:takeOrder_id>', views.delete_takeOrder, name='delete_takeOrder'),
    path('delete_take<int:takeOrder_id>', views.delete_take, name='delete_take'),
    
    path('export-data/', views.export_data_view, name='export_data'),
    path('import-data/', views.import_data_view, name='import_data'),
    
    path('export-all-data/', views.export_all_data_view, name='export_all_data'),
    path('import-all-data/', views.import_all_data_view, name='import_all_data'),
    path('clear-database/', views.clear_database_view, name='clear_database'),

]