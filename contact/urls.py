from django.urls import path
from . import views
urlpatterns = [
    path('', views.contact, name='contact'),
    path('contact', views.contact, name='contact'),
    path('<int:contact_id>', views.contact_detail, name='contactdetail'),
]
