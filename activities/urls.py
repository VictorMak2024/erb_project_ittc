from django.urls import path
from . import views

urlpatterns = [
    path('', views.activities, name='activities'),
    path('<int:activity_id>', views.activity, name='activity'),
<<<<<<< HEAD
    #path('search', views.search, name='search'),
=======
#    path('search', views.search, name='search'),
>>>>>>> origin/WCNgApps

]