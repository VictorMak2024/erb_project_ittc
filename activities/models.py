from django.db import models
from datetime import datetime
from salesmens.models import Salesmen
from .choices import medium_choices

# Create your models here.

#reference 
# https://www.hkpc.org/en/hkpc-spotlights/events/corporate-events
# https://campaigninfo.hkpc.org/register-new-innovation-technology-studymission-germanyfrance
class Activity(models.Model):
    salesmen = models.ForeignKey(Salesmen, on_delete=models.DO_NOTHING)
    hotitem = models.BooleanField(default=False)
    title = models.CharField(blank=False)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    date_start = models.DateField(default=datetime.now, blank=True) #()format ='%d-%month-%Y'?
    date_end = models.DateField(default=datetime.now, blank=True) #()format ='%d-%month-%Y'?
    time_start = models.TimeField(default=datetime.now, blank=True) #time schedule?
    time_end = models.TimeField(default=datetime.now, blank=True) #time schedule?
    location = models.CharField(max_length=50) #is it neeed using choices?
    medium = models.CharField(max_length=50, choices=medium_choices.items())
    target = models.CharField(max_length=200) #is it neeed using choices?
    trainer = models.CharField(max_length=50)# is it need using choices?
    price = models.IntegerField(default=0)
    total_sit = models.IntegerField(default=0)
    onenquiry_sit = models.IntegerField(default=0)
    phaseOut = models.BooleanField(default=False)

    def __str__(self):
        return self.name
<<<<<<< HEAD
=======
# Create your models here.

>>>>>>> origin/WCNgApps
