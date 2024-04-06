from django.db import models
from django.contrib.auth.models import User
import datetime
from  django.utils import timezone
from livestock.models import Livestock
from FMS.mixins import NameMixin, AgeMixin, GenderMixin

    
class Employee(NameMixin, AgeMixin, GenderMixin, models.Model):
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    hire_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    # def __str__(self):
    #     return f'{self.first_name} {self.last_name}'

    def __str__(self):
       return f'{self.name}'
    
    class Meta: 
        ordering = ['first_name', 'last_name']

    
class MilkProduction(models.Model):
    cow = models.ForeignKey(Livestock, on_delete=models.CASCADE, verbose_name="Cow")
    milking_date = models.DateField(verbose_name="Milking Date")
    morning_volume  = models.DecimalField(max_digits=2, decimal_places=2, verbose_name="Morning Volume (liters)")
    evening_volume  = models.DecimalField(max_digits=2, decimal_places=2, verbose_name="Evening Volume (liters)")

    class Meta:
        verbose_name = "Milk Production"
    
    def __str__(self):
        return f"{self.cow.name} - {self.milking_date}"


class Feed(models.Model):
    FEED_TYPE_CHOICES = [
        ('hay', 'Hay'),
        ('silage', 'Silage'),
        ('dairymeal', 'Dairy Meal'),
        ('other', 'Other'),
    ]
    name = models.CharField(max_length=100)
    feed_type = models.CharField(max_length=20, choices=FEED_TYPE_CHOICES, default='other')
    description = models.TextField(blank=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=20)
    expiration_date = models.DateField(blank=True, null=True)
    purchase_date = models.DateField()
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    supplier = models.CharField(max_length=100)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

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
class Inventory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=20)
    location = models.CharField(max_length=100, blank=True)
    minimum_stock_level = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def update_quantity_from_consumption_records(self):
        """
        Update the quantity of the feed item based on feed consumption records.
        """
        total_consumed = FeedConsumption.objects.filter(feed_item=self).aggregate(total=models.Sum('quantity_consumed'))['total']
        if total_consumed is not None:
            self.quantity -= total_consumed
            self.save()
    
class FeedConsumption(models.Model):
    feed_item = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    livestock = models.ForeignKey(Livestock, on_delete=models.CASCADE)
    date_consumed = models.DateField(default=timezone.now)
    quantity_consumed = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        # Update the available quantity of the feed item after consumption
        self.feed_item.quantity -= self.quantity_consumed
        self.feed_item.save()
        super().save(*args, **kwargs)


# class Field(models.Model):     
#     species = models.CharField(blank=False, max_length=80, default='')

# class Task(models.Model):
#     species = models.CharField(blank=False, max_length=80, default='')

# class Equipment(models.Model):
#     species = models.CharField(blank=False, max_length=80, default='')

# class Expense(models.Model):
#     type = 
    
# class Income(models.Model):
    
# class Health(models.Model):
#     animal = models.ForeignKey(Livestock)
#     date = models.DateField()
#     type - models.CharField()
#     description = models.CharField()
#     consultant = models.ForeignKey(User)


# class Ownership(models.Model)
#     owner = models.ForeignKey
#     entity = models.CharField()
#     date_acquired = models.DateField
#     date_sold = models.DateField