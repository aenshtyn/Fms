from django.db import models

import datetime
# from django.contrib.auth.models import User
from  django.utils import timezone
from FMS.mixins import AgeMixin, GenderMixin

# Create your models here.
class Livestock(AgeMixin, GenderMixin, models.Model):

    SPECIES_CHOICES = [
        ('cattle', 'Cattle'),
        ('sheep', 'Sheep'),
        ('goat', 'Goat'),
        ('poultry', 'Poultry'),
        ('others', 'Others'),
    ]

    species = models.CharField(blank=False, max_length=80, choices=SPECIES_CHOICES, default='cattle')
    breed = models.CharField(blank=False, max_length=80, default='')
    date_of_birth = models.DateField()
    # owner = models.ForeignKey(User, on_delete=models.CASCADE)  # Assuming each livestock belongs to a user
    date_acquired = models.DateField(blank=True, null=True)
    acquisition_source = models.CharField(blank=True, max_length=100)
    acquisition_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    date_sold = models.DateField(blank=True, null=True)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    health_status = models.CharField(blank=True, max_length=100)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name if self.name else f'{self.species} ({self.breed})'
    
class HealthRecord(models.Model):
    cow = models.ForeignKey(Livestock, on_delete=models.CASCADE)
    date = models.DateField()
    condition = models.CharField(max_length=100)
    treatment = models.TextField()

    def __str__(self):
        return f"{self.cow.name} - {self.date}"
    

# class MilkProduction(models.Model):
#     cow = models.ForeignKey(Livestock, on_delete=models.CASCADE, verbose_name="Cow")
#     milking_date = models.DateField(verbose_name="Milking Date")
#     morning_volume  = models.DecimalField(max_digits=2, decimal_places=2, verbose_name="Morning Volume (liters)")
#     evening_volume  = models.DecimalField(max_digits=2, decimal_places=2, verbose_name="Evening Volume (liters)")

#     class Meta:
#         verbose_name = "Milk Production"
    
#     def __str__(self):
#         return f"{self.cow.name} - {self.milking_date}"