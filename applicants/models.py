from django.db import models
from datetime import datetime
# Create your models here.
class Applicant(models.Model):
    #job = models.CharField(max_length=200)
    job_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    # work_experience = models.TextField(blank=True)
    # qualification = models.TextField(blank=True) 
    # expected_salary = models.CharField(max_length=100)
    # date_available = models.DateTimeField(default=datetime.now, blank=True)

    apply_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField()
    company = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=100, blank=True)
    cv_file = models.FileField(upload_to='cv/', blank=True)
    def __str__(self):
        return self.name

# Create your models here.
