from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Parcel(models.Model):
    
    parcel_number = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    size = models.DecimalField(max_digits=10, decimal_places=2)  # Use DecimalField for precise measurements
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the user who owns the parcel
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the parcel

    def __str__(self):
        return f"Parcel {self.number}"
    
class Usage(models.Model):
    USAGE_OPTIONS = [
        ('feedlot', 'Feedlot'),
        ('agriculture', 'Agriculture'),
        ('grazing', 'Grazing'),
        ('aquaculture', 'Aquaculture'),
    ]

    parcel = models.ForeignKey(Parcel, on_delete=models.CASCADE)
    use_type = models.CharField(max_length=50, choices=USAGE_OPTIONS)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return f"Usage History for Parcel {self.parcel.number}"
    
class Maintenance(models.Model):
    parcel = models.ForeignKey(Parcel, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    description = models.TextField()

    def __str__(self):
        return f"Maintenance History for Parcel {self.parcel.number}"
