from django.db import models
import datetime
from  django.utils import timezone

# Create your models here.
class NameMixin:
    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'
    
class AgeMixin:
    @property
    def age(self):
        today = timezone.now()
        dob = self.dob

        years = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        months = today.month - dob.month - (today.day < dob.day)

        if months < 0: months += 12 
        years -= 1
        age_str = ''
        if years > 0:
            age_str += f'{years} {"year" if years == 1 else "years"}'
            if months > 0:
                age_str += ' '
        if months > 0:
            age_str += f'{months} {"month" if months == 1 else "months"}'

        if not age_str:
            age_str = "less than a month"

        return age_str
    
class Worker(NameMixin, AgeMixin, models.Model):
    first_name = models.CharField(blank=False, max_length=80, default='')
    last_name = models.CharField(blank=False, max_length=80, default='')
    dob = models.DateField()
    gender = models.CharField(blank=False, max_length=80, default='')
    date_joined = models.DateField()

    def __str__(self):
       return f'{self.name}'
    
    class Meta: 
        ordering = ['first_name', 'last_name']