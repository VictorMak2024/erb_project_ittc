from django.urls import path
from . import views

# related to templates (.html)
urlpatterns = [
    path('register_login', views.register_login, name='register_login'),
        path('dashboard', views.dashboard, name='dashboard'),
]