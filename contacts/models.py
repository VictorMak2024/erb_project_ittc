from django.db import models
from datetime import datetime
from activities.models import Activity
from courses.models import Course
from products.models import Product
# Create your models here.
class Activity_Contact(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)  # Link to Activity model
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
    course = models.ForeignKey(Course, on_delete=models.CASCADE) 
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
    product = models.ForeignKey(Product, on_delete=models.CASCADE) 
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField()
    def __str__(self):
        return self.name

class TakeOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE) 
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    onOrderQty = models.IntegerField(default=0)
    salesmen_id = models.IntegerField()
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField()
    def __str__(self):
        return self.name