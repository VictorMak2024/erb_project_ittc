from django.urls import path
from . import views

# related to templates (.html)
urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
<<<<<<< HEAD
    path('dashboard', views.dashboard, name='dashboard')
=======
    path('dashboard', views.dashboard, name='dashboard'),
    path('shoppingCart', views.shoppingCart, name='shoppingCart'),
    path('confirmOrder', views.confirmOrder, name='confirmOrder'),
    path('remove_from_cart/<int:order_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('shoppingCartOrders', views.shoppingCartOrders, name='shoppingCartOrders'),  # New URL

>>>>>>> refs/remotes/origin/main
]