from django.db import models
from datetime import datetime

# Create your models here.
class Activity_Contact(models.Model):
    activity = models.CharField(max_length=200)
    activity_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField()
    is_paid = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class Course_Contact(models.Model):
    course = models.CharField(max_length=200)
    course_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField()
    is_paid = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    
class Product_Contact(models.Model):
    product = models.CharField(max_length=200)
    product_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField()
    def __str__(self):
        return self.name

