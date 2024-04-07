from django.db import models
from  django.utils import timezone

# Create your models here.
class PersonDetailsMixin(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20)
    address = models.TextField()

    class Meta:
        abstract = True

    class Meta:
        abstract = True
    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'
    
class AgeMixin(models.Model):
    date_of_birth = models.DateField()

    class Meta:
        abstract = True

    @property
    def age(self):
        today = timezone.now()
        dob = self.date_of_birth

        years = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        months = today.month - dob.month - (today.day < dob.day)

        if months < 0: 
            months += 12
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
class GenderMixin(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    gender = models.CharField(blank=False, max_length=80, choices=GENDER_CHOICES, default='male')

    class Meta:
        abstract = True

   