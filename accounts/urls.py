from django.urls import path
from . import views

# related to templates (.html)
urlpatterns = [
    path('register_login', views.register_login, name='register_login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('shoppingCart', views.shoppingCart, name='shoppingCart'),
    path('confirmOrder', views.confirmOrder, name='confirmOrder'),
    path('remove_from_cart/<int:order_id>/', views.remove_from_cart, name='remove_from_cart'),

]