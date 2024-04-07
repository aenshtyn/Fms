from django.db import models
from FMS.mixins import PersonDetailsMixin, AgeMixin, GenderMixin

# Create your models here.
class Client(PersonDetailsMixin, AgeMixin, GenderMixin, models.Model):

    company = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"