from django.urls import path
from . import views
urlpatterns = [
    path('newsevents', views.newsevents, name = 'newsevents'),
    path('search_news',views.search_news, name = 'search_news')
]
