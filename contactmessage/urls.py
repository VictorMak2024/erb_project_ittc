from django.urls import path
from . import views
urlpatterns= [
    #path('contactmessage', views.contactmessage, name='contactmessage'),
    path('contactus/<int:contact_id>', views.contactmessage, name='contactmessage'),
]