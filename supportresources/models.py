from django.db import models
from datetime import datetime
from srdetails.models import Srdetail

class SupportResource(models.Model):
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    web_url = models.URLField(max_length=500, blank=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    sr_items = models.ForeignKey(Srdetail, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.title
