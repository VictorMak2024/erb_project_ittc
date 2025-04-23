from django.db import models
from datetime import datetime
from contacts.models import TakeOrder
from salesmens.models import Salesmen
from .choices import district_choices

# Create your models here.
class ShoppingCart(models.Model):
    user_id = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING, null=True, blank=True)
    orders = models.ManyToManyField(TakeOrder)  # Link to multiple TakeOrder entries
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    address = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    district = models.CharField(max_length=50, choices=district_choices.items())
    description = models.TextField(blank=True)
    total_Amount = models.IntegerField(default=0)
    is_shipped = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    order_date = models.DateTimeField(default=datetime.now, blank=True)
    ship_date = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return f"ShoppingCart for User {self.user_id}"
