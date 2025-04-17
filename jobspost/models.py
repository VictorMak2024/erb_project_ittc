from django.db import models
from datetime import datetime
# Create your models here.
class Jobs(models.Model):
    title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=20, choices=[
        ('Full time', 'Full time'),
        ('Part time', 'Part time'),
        ('Contract', 'Contract'),
        ('Internship', 'Internship'),
        ('Temporary', 'Temporary'),
    ])
    salary = models.IntegerField()
    post_date = models.DateTimeField(default=datetime.now,blank=True)
    
    location = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    logo_url = models.URLField(max_length=500, blank=True)  

    responsibilities = models.TextField()
    requirement = models.TextField()
    email = models.CharField(max_length=100, default="atkincheung@yahoo.com.hk")

    def __str__(self):
        return self.title