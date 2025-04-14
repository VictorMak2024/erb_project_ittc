from django.urls import path
from . import views

urlpatterns = [
    path('', views.activities, name='activities'),
    path('<int:activity_id>', views.activity, name='activity'),
#    path('search', views.search, name='search'),

]