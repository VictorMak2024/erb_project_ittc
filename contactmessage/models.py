from django.db import models
from contact.models import Contact
# Create your models here.
from datetime import datetime

# Create your models here.
class Contactmessage(models.Model):
    center = models.CharField(max_length=200)
    # contactmessage_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField()
    post_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField()
    def __str__(self):
        return f"Message from {self.name}: {self.message}"
