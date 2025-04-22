from django.db import models
from datetime import datetime
from salesmens.models import Salesmen
from .choices import medium_choices

# Create your models here.

#reference https://www.hkpc.org/en/hkpc-academy/latest-training-programmes
# https://www.hkpcacademy.org/en/f0001204-ai-gym-001/?__hstc=245001754.bb963f057cb3f85aa80c154737154f4c.1741876631108.1743153486748.1743514062268.4&__hssc=245001754.2.1743514062268&__hsfp=948960675
# https://www.hkpcacademy.org/en/programme-search/

class Course(models.Model):
    salesmen = models.ForeignKey(Salesmen, on_delete=models.DO_NOTHING)
    hotitem = models.BooleanField(default=False)
    title = models.CharField(blank=False)
    name = models.CharField(max_length=50) # make reference no?
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
<<<<<<< HEAD
        return self.title
=======
        return self.title
>>>>>>> origin/WCNgApps
