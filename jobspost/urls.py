from django.urls import path
from . import views
urlpatterns = [
    path('', views.jobspost, name='jobspost'),
    path('<int:job_id>', views.jobspost_detail, name='jobspost_detail'),
    path('search', views.search, name='search'),
]
