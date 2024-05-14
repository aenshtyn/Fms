from django.db import models
from  django.utils import timezone
from FMS.mixins import AgeMixin, GenderMixin
from datetime import timedelta
from django.core.exceptions import ValidationError

# Create your models here.
class Animal(AgeMixin, GenderMixin, models.Model):
    """ Represents farm animals with details like species, breed, health, and ownership. """

    SPECIES_CHOICES = [
        ('cattle', 'Cattle'),
        ('sheep', 'Sheep'),
        ('goat', 'Goat'),
        ('poultry', 'Poultry'),
        ('others', 'Others'),
    ]

    HEALTH_STATUS_CHOICES = [
        ('healthy', 'Healthy'),
        ('sick', 'Sick'),
        ('injured', 'Injured'),
        ('recovering', 'Recovering'),
        ('unknown', 'Unknown'),
    ]
    id_number = models.CharField(max_length=50, blank=True, null=True, unique=True, db_index=True)
    species = models.CharField(blank=False, max_length=80, choices=SPECIES_CHOICES, default='cattle')
    breed = models.CharField(blank=False, max_length=80, default='')
    date_of_birth = models.DateField()
    current_location = models.CharField(max_length=100, blank=True, null=True)
    # owner = models.ForeignKey(User, on_delete=models.CASCADE)  # Assuming each Animal belongs to a user
    date_acquired = models.DateField(blank=True, null=True)
    acquisition_source = models.CharField(blank=True, max_length=100)
    acquisition_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    date_sold = models.DateField(blank=True, null=True)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    health_status = models.CharField(max_length=100, choices=HEALTH_STATUS_CHOICES, default='healthy')
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['id_number']
        verbose_name_plural = "animals"

    def is_lactating_cow(self):
        return self.species == 'cattle' and self.gender == 'female'
    
    @staticmethod
    def get_lactating_cows():
        lactating_animals = Animal.objects.filter(species='cattle', gender='female', )
        return lactating_animals
    
    def __str__(self):
        return self.id_number if self.id_number else f'{self.species} ({self.breed})'
    
    def clean(self):
        # Custom validation to ensure dates are logical
        if self.date_of_birth and self.date_acquired:
            if self.date_of_birth > self.date_acquired:
                raise ValidationError("Date of birth cannot be after date acquired.")
        if self.date_of_birth > timezone.now().date():
            raise ValidationError("Date of birth cannot be in the future.")

class Health(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    date = models.DateField()
    condition = models.CharField(max_length=100)
    treatment = models.TextField(blank=True)
    symptoms = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "health records"

    def __str__(self):
        return f"{self.animal.id_number} - {self.date} - {self.condition}"
    
class Breeding(models.Model):
    animal = models.ForeignKey(Animal, related_name='breedings', on_delete=models.CASCADE)
    mate = models.ForeignKey(Animal, related_name='mated_with', on_delete=models.CASCADE)
    mating_date = models.DateField()

    class Meta:
        verbose_name_plural = "breeding records"

    def __str__(self):
        return f"{self.animal} - Mated with {self.mate} - Expected Due Date: {self.expected_due_date()}"
    
    def expected_due_date(self):
        species_gestation_periods = {
            'cattle': 280,
            'sheep': 147,
            'goat': 150,
        }
        return self.mating_date + timedelta(days=species_gestation_periods.get(self.animal.species, 0))


class Reproduction(models.Model):
    animal = models.OneToOneField(Animal, on_delete=models.CASCADE)
    estrus_detection_date = models.DateField()
    pregnancy_status = models.BooleanField(default=False)
    calving_date = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "reproduction records"

    def __str__(self):
        return f"{self.animal} - Estrus Detection: {self.estrus_detection_date} - Pregnancy: {self.pregnancy_status}"

class Vaccination(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    vaccine_name = models.CharField(max_length=100)
    date_administered = models.DateField()
    dosage = models.CharField(max_length=50)
    
    class Meta:
        verbose_name_plural = "vaccinations"

    def __str__(self):
        return f"{self.animal} - {self.vaccine_name} - Administered on {self.date_administered}"
    
class Mortality(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    date = models.DateField()
    cause_of_death = models.CharField(max_length=100)
    disposal_method = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "mortalities"

    def __str__(self):
        return f"{self.animal} - Died on {self.date} - Cause: {self.cause_of_death}"