from django.db import models
from salesmens.models import Salesmen
from . choices import title_choices, operation_choices, control_choices, power_choices, automation_choices, application_choices

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50, blank=True) # choices=title_choices.items())
    description = models.TextField(blank=True)
    photos = models.ImageField(upload_to='photos/%y/%m/%d/')
    def __str__(self):
        return self.title

class Product(models.Model):
    hotitem = models.BooleanField(default=False)
    salesmen = models.ForeignKey(Salesmen, on_delete=models.DO_NOTHING)
    title = models.ForeignKey(Category, on_delete=models.DO_NOTHING,default=1)
    no = models.CharField(max_length=50)
    operation = models.CharField(max_length=50, choices=operation_choices.items())
    control = models.CharField(max_length=50, choices=control_choices.items())
    automation = models.CharField(max_length=50, choices=automation_choices.items())
    application = models.CharField(max_length=50, choices=application_choices.items())
    power = models.CharField(max_length=50, choices=power_choices.items())
    description = models.TextField(blank=True)
    price = models.IntegerField()
    stockQty = models.IntegerField(default=0)
    onOrderQty = models.IntegerField(default=0)
    phaseOut = models.BooleanField(default=False)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)


    def __str__(self):
        return self.no
    
    #reference : https://reeman.en.made-in-china.com/product-group/LMfAghFdgurt/Cleaning-Robot-catalog-1.html?pv_id=1ing0sghfe6b&faw_id=1ing0skvc179
    # https://dexforce.en.made-in-china.com/product/sQGrznqKaPRF/China-Robot-Arm-Palletizing-Station-with-Vision-Camera-as-Guidance.html?pv_id=1ing8uff6fe6&faw_id=1ing8uhn55f9
    # https://www.szghauto.com/product/28/
    # https://www.reemanrobot.com/?gad_source=1&gclid=Cj0KCQjwhr6_BhD4ARIsAH1YdjC2ys5YS9CzJAR00Gqp5C2S0Rkz4IlVDl2HknNDq6AFkEBhZri6uiUaAgyZEALw_wcB
    # https://www.seer-robotics.ai/amr-list
    # https://www.szghauto.com/product/28/
    # https://www.keenon.com/en/product/C30/index.html?gad_source=1&gclid=Cj0KCQjwhr6_BhD4ARIsAH1YdjDTyY_y_oOCCUjs-2NzGJcTwoP70L9fCDeQ4FzS1ql9QHhqoFYcXbsaAiWkEALw_wcB
    # https://avidbots.com/robots/meet-neo/
# Create your models here.
