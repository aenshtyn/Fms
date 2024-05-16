from django.db import models
from django.core.exceptions import ValidationError
from inventory.models import Product, Category

# Create your models here.
# from FMS.mixins import , AgeMixin, GenderMixin

class Crop(models.Model):

    USE_CHOICES = [
        ('animal_feed', 'Animal Feed'),
        ('human_consumption', 'Human Consumption'),
    ]
    
    UNIT_CHOICES = [
        ('kg', 'Kilograms'),
        ('tonnes', 'Tonnes'),
        ('bushels', 'Bushels'),
        ('pounds', 'Pounds'),
        ('liters', 'Liters'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    variety = models.CharField(max_length=100, blank=True, null=True)
    crop_use = models.CharField(max_length=20, choices=USE_CHOICES, default = 'human_consumption')
    planting_date = models.DateField()
    harvest_date = models.DateField()
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=50, choices=UNIT_CHOICES, default = 'kg')
    location = models.CharField(max_length=100, blank=True, null=True)
    notes = models.TextField(blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='crop_productions', blank=True, null=True)  # Indicates if the crop becomes feed for livestock

    # Additional fields specific to crop management can be added here

    class Meta:
        verbose_name_plural = "Crops"
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['planting_date']),
            models.Index(fields=['harvest_date']),
            models.Index(fields=['category']),
        ]

    def save(self, *args, **kwargs):
        # Automatically associate the production with the appropriate product
        if not self.product:
            category, created = Category.objects.get_or_create(name='Crops')
            self.product, created = Product.objects.get_or_create(
                name=self.crop_type,
                defaults={'category': category, 'unit_price': 0, 'sku': f'{self.crop_type.upper()}-001'}
            )
        super().save(*args, **kwargs)   

    def __str__(self):
        if self.variety:
            return f"{self.name} - {self.variety}"
        return self.name

    def clean(self):
        if self.planting_date > self.harvest_date:
            raise ValidationError("Planting date cannot be after harvest date.")

class CropCycle(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    notes = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Crop Cycles"

    def __str__(self):
        return f"{self.crop.name} Cycle ({self.start_date} - {self.end_date})"
    
    def clean(self):
        if self.start_date > self.end_date:
            raise ValidationError("Start date cannot be after end date.")

class CropHealth(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    date = models.DateField()
    condition = models.CharField(max_length=100)
    treatment = models.TextField()

    class Meta:
        verbose_name_plural = "Crop Health Records"

    def __str__(self):
        return f"{self.crop.name} - {self.date}"
    

class Harvest(models.Model):

    UNIT_CHOICES = [
        ('kg', 'Kilograms'),
        ('tonnes', 'Tonnes'),
        ('bushels', 'Bushels'),
        ('pounds', 'Pounds'),
        ('liters', 'Liters'),
        ('other', 'Other'),
    ]

    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    date = models.DateField()
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=50, choices=UNIT_CHOICES, default='kg')
    notes = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Harvests"
        indexes = [
            models.Index(fields=['date']),
            models.Index(fields=['quantity']),
        ]

    def __str__(self):
        return f"{self.crop.name} Harvest - {self.date}"
    
class PestControl(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    date = models.DateField()
    pest_type = models.CharField(max_length=100)
    control_method = models.TextField()

    class Meta:
        verbose_name_plural = "Pest Controls"

    def __str__(self):
        return f"{self.crop.name} - {self.date} - {self.pest_type}"