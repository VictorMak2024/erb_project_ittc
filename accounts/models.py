from django.db import models
from datetime import datetime
from salesmens.models import Salesmen
from .choices import district_choices

# Create your models here.
class ShoppingCart(models.Model):
    salesmen = models.ForeignKey(Salesmen, on_delete=models.DO_NOTHING)
    user_id = models.IntegerField()
    name = models.CharField(max_length=200)
    order_no = models.CharField(max_length=50)
    is_paid = models.BooleanField(default=True)
    is_completed = models.BooleanField(default=True)
    cancelled = models.BooleanField(default=True)
    no_1 = models.CharField(max_length=50)
    title_1 = models.CharField(max_length=50)
    price_1 = models.IntegerField()
    onOrderQty_1 = models.IntegerField(default=0)
    no_1 = models.CharField(max_length=50)
    title_1 = models.CharField(max_length=50)
    price_2 = models.IntegerField()
    onOrderQty_2 = models.IntegerField(default=0)
    no_3 = models.CharField(max_length=50)
    title_3 = models.CharField(max_length=50)
    price_3 = models.IntegerField()
    onOrderQty_3 = models.IntegerField(default=0)
    no_4 = models.CharField(max_length=50)
    title_4 = models.CharField(max_length=50)
    price_4 = models.IntegerField()
    onOrderQty_4 = models.IntegerField(default=0)
    no_5 = models.CharField(max_length=50)
    title_5 = models.CharField(max_length=50)
    price_5 = models.IntegerField()
    onOrderQty_5 = models.IntegerField(default=0)
    no_6 = models.CharField(max_length=50)
    title_6 = models.CharField(max_length=50)
    price_6 = models.IntegerField()
    onOrderQty_6 = models.IntegerField(default=0)
    address = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    district = models.CharField(max_length=50, choices=district_choices.items())
    description = models.TextField(blank=True)
    order_date = models.DateTimeField(default=datetime.now, blank=True)
    ship_date = models.DateTimeField(blank=True)

    def __str__(self):
        return self.order_no
