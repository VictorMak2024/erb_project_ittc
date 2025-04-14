from django.urls import path
from . import views
urlpatterns = [
    path('applicant', views.applicant, name='applicant'),
]
# Compare this snippet from contacts/views.py: