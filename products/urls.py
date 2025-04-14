from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('category/<str:category_title>', views.products, name='products_by_category'),
    path('<int:product_id>', views.product, name='product'),
    path('search', views.search, name='search'),

]
