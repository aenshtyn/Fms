from django.db import models

# Create your models here.
# from FMS.mixins import , AgeMixin, GenderMixin

class Crop(models.Model):
    name = models.CharField(max_length=100)
    variety = models.CharField(max_length=100, blank=True, null=True)
    planting_date = models.DateField()
    harvest_date = models.DateField()
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=50)
    location = models.CharField(max_length=100, blank=True, null=True)
    notes = models.TextField(blank=True)

    feeds_livestock = models.BooleanField(default=False)  # Indicates if the crop becomes feed for livestock

    # Additional fields specific to crop management can be added here

    def __str__(self):
        if self.variety:
            return f"{self.name} - {self.variety}"
        return self.name


class CropCycle(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.crop.name} Cycle ({self.start_date} - {self.end_date})"

class CropHealth(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    date = models.DateField()
    condition = models.CharField(max_length=100)
    treatment = models.TextField()

    def __str__(self):
        return f"{self.crop.name} - {self.date}"
    

class Harvest(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    date = models.DateField()
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.crop.name} Harvest - {self.date}"
    
class PestControl(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    date = models.DateField()
    pest_type = models.CharField(max_length=100)
    control_method = models.TextField()

    def __str__(self):
        return f"{self.crop.name} - {self.date} - {self.pest_type}"