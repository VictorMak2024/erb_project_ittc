from django.urls import path
from . import views

# ''<- url endpoint, views<- function , in this case, index fucnction in views; '' is endpoint
urlpatterns = [
    path('', views.index, name='index'),
]