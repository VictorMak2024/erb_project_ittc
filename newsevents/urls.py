from django.urls import path
from . import views
urlpatterns = [
    path('newsevents', views.newsevents, name = 'newsevents'),
    path('<int:news_id>', views.newsevents_detail, name = 'newsevents_detail'),
    path('search',views.search, name = 'search')
]
