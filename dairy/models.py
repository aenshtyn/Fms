from django.db import models

import datetime
# from django.contrib.auth.models import User
from  django.utils import timezone
from livestock.models import Livestock
class MilkProduction(models.Model):
    cow = models.ForeignKey(Livestock, on_delete=models.CASCADE, verbose_name="Cow")
    milking_date = models.DateField(verbose_name="Milking Date")
    morning_volume  = models.DecimalField(max_digits=2, decimal_places=2, verbose_name="Morning Volume (liters)")
    evening_volume  = models.DecimalField(max_digits=2, decimal_places=2, verbose_name="Evening Volume (liters)")

    class Meta:
        verbose_name = "Milk Production"
    
    def __str__(self):
        return f"{self.cow.name} - {self.milking_date}"
    
class DairyFeeds(models.Model):
    date = models.DateField()
    feed_type = models.CharField()
    quantity = models.DecimalField(max_digits=3, decimal_places=2)
    