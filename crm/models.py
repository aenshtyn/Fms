from django.db import models
from FMS.mixins import PersonDetailsMixin, AgeMixin, GenderMixin

# Create your models here.
class Client(PersonDetailsMixin, AgeMixin, GenderMixin, models.Model):

    def __str__(self):
        return f"{self.name}"