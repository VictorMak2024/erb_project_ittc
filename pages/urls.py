from django.urls import path
from . import views

# ''<- url endpoint, views<- function , in this case, index fucnction in views; '' is endpoint
urlpatterns = [
    path('', views.index, name='index'),
    path('about',views.about, name='about'),
    path('team',views.team, name='team'),
    path('victor',views.victor, name='victor'),
    path('tommy',views.tommy, name='tommy'),
    path('wc',views.wc, name='wc'),
]