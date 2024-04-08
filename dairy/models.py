from django.db import models
from livestock.models import Animal
class MilkProduction(models.Model):
    cow = models.ForeignKey(Animal, on_delete=models.CASCADE, verbose_name="Cow")
    milking_date = models.DateField(verbose_name="Milking Date")
    morning_volume  = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Morning Volume (liters)")
    evening_volume  = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Evening Volume (liters)")

    class Meta:
        verbose_name = "Milk Production"

    def total_volume(self):
        return self.morning_volume + self.evening_volume
    
    def __str__(self):
        return f"{self.cow.id_number} - {self.milking_date}"
    
class DairyFeeds(models.Model):
    FEED_TYPE_CHOICES = [
        ('hay', 'Hay'),
        ('silage', 'Silage'),
        ('dairymeal', 'Dairy Meal'),
        ('other', 'Other'),
    ]
    date = models.DateField()
    feed_type = models.CharField(max_length=20, choices=FEED_TYPE_CHOICES, verbose_name="Feed Type")
    quantity = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Quantity (kg)")

    class Meta:
        verbose_name = "Dairy Feed"
        verbose_name_plural = "Dairy Feeds"
