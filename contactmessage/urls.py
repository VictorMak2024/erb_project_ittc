from django.urls import path
from . import views
urlpatterns= [
    path('contactmessage', views.contactmessage, name='contactmessage'),
    
]