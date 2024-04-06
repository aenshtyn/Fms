from django.db import models

import datetime
from django.contrib.auth.models import User
from  django.utils import timezone
from FMS.mixins import NameMixin, AgeMixin, GenderMixin

# Create your models here.
class Livestock(NameMixin, AgeMixin, GenderMixin, models.Model):

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
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  # Assuming each livestock belongs to a user
    date_acquired = models.DateField(blank=True, null=True)
    acquisition_source = models.CharField(blank=True, max_length=100)
    acquisition_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    date_sold = models.DateField(blank=True, null=True)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    health_status = models.CharField(blank=True, max_length=100)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name if self.name else f'{self.species} ({self.breed})'