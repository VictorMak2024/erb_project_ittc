from django.db import models
from datetime import datetime   
# Create your models here.
class Newsevents(models.Model):
    title = models.CharField(max_length=200)
    post_date = models.DateTimeField(default=datetime.now,blank=True)
    location = models.CharField(max_length=100)
    is_News = models.BooleanField(default=False)
    is_Events = models.BooleanField(default=True)
    iframe = models.CharField(max_length=600, null=True, blank=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True, blank=True)
    detail = models.TextField()
    def __str__(self):
        return self.title