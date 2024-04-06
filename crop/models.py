from django.db import models

# Create your models here.
from FMS.mixins import NameMixin, AgeMixin, GenderMixin

class Crop(models.Model):
    name = models.CharField(max_length=100)
    variety = models.CharField(max_length=100, blank=True, null=True)
    planting_date = models.DateField()
    harvest_date = models.DateField()
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=50)
    location = models.CharField(max_length=100, blank=True, null=True)
    notes = models.TextField(blank=True)

    feeds_livestock = models.BooleanField(default=False)  # Indicates if the crop becomes feed for livestock

    # Additional fields specific to crop management can be added here

    def __str__(self):
        if self.variety:
            return f"{self.name} - {self.variety}"
        return self.name