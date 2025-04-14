from django.db import models
from datetime import datetime   
# Create your models here.
class Newsevents(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(default=datetime.now,blank=True)
    location = models.CharField(max_length=100)
    image_url = models.URLField(max_length=500, blank=True)
    def __str__(self):
        return self.title