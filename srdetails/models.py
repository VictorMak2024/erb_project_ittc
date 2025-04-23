from django.db import models
from datetime import datetime

class Srdetail(models.Model):
    itemsname = models.CharField(max_length=200)
    items_no = models.CharField(max_length=200)
    

    def __str__(self):
        return self.itemsname