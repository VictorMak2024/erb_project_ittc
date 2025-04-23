from django.urls import path
from . import views
urlpatterns = [
    path('', views.teaminfo, name = 'teaminfo'),
    path('<int:team_id>', views.teaminfo_detail, name = 'teamdetail'),
]