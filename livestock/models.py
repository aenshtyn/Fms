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
    identification_number = models.CharField(max_length=50, blank=True, null=True)
    current_location = models.CharField(max_length=100, blank=True, null=True)
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
    
class Health(models.Model):
    animal = models.ForeignKey(Livestock, on_delete=models.CASCADE)
    date = models.DateField()
    condition = models.CharField(max_length=100)
    treatment = models.TextField(blank=True)

    def __str__(self):
        return f"{self.cow.name} - {self.date}"
    
class Breeding(models.Model):
    animal = models.ForeignKey(Livestock, related_name='breeding_s', on_delete=models.CASCADE)
    mate = models.ForeignKey(Livestock, related_name='mates', on_delete=models.CASCADE)
    mating_date = models.DateField()
    expected_due_date = models.DateField()

    def __str__(self):
        return f"{self.animal} - Mated with {self.mate} - Expected Due Date: {self.expected_due_date}"
    
class Reproduction(models.Model):
    animal = models.OneToOneField(Livestock, on_delete=models.CASCADE)
    estrus_detection_date = models.DateField()
    pregnancy_status = models.BooleanField(default=False)
    calving_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.animal} - Estrus Detection: {self.estrus_detection_date} - Pregnancy: {self.pregnancy_status}"

class Vaccination(models.Model):
    animal = models.ForeignKey(Livestock, on_delete=models.CASCADE)
    vaccine_name = models.CharField(max_length=100)
    date_administered = models.DateField()
    dosage = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.animal} - {self.vaccine_name} - {self.date_administered}"
    
class Mortality(models.Model):
    animal = models.ForeignKey(Livestock, on_delete=models.CASCADE)
    date = models.DateField()
    cause_of_death = models.CharField(max_length=100)
    disposal_method = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.animal} - Date of Death: {self.date} - Cause: {self.cause_of_death}"