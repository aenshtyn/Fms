from django.db import models
from FMS.mixins import NameMixin, AgeMixin, GenderMixin

# Create your models here.
class Crm(NameMixin, AgeMixin, GenderMixin, models.Model):

    def __str__(self):
        return f"{self.name}"