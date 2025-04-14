from django.db import models

# Create your models here.
class Contact(models.Model):
    contact_id = models.IntegerField()
    center = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    fax = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    office_hours = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    iframe = models.CharField(max_length=600)
    def __str__(self):
        return self.center
