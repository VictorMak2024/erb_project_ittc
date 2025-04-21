from django.db import models

# Create your models here.
class Teams(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True, blank=True)
    duty = models.CharField(max_length=200)
    detail = models.TextField()
    def __str__(self):
        return self.name