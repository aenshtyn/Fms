from django.db import models
from django.core.exceptions import ValidationError
from livestock.models import Animal
from django.db.models import Sum
class Production(models.Model):
    cow = models.ForeignKey(Animal, on_delete=models.CASCADE, verbose_name="Cow", related_name="productions")
    milking_date = models.DateField(verbose_name="Milking Date")
    morning_volume  = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Morning Volume (liters)",default=0.00)
    evening_volume  = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Evening Volume (liters)", default=0.00)

    class Meta:
        verbose_name = "Milk Production"
        unique_together = ('cow', 'milking_date')  # Ensures one record per cow per day

    @classmethod
    def day_total_volume(cls, milking_date):
        """Calculate total morning and evening milk volume for a given date."""
        volumes = cls.objects.filter(milking_date=milking_date).aggregate(
            total_morning_volume=Sum('morning_volume'),
            total_evening_volume=Sum('evening_volume')
        )
        total_days_volume = (volumes['total_morning_volume'] or 0) + (volumes['total_evening_volume'] or 0)
        return volumes['total_morning_volume'] or 0, volumes['total_evening_volume'] or 0, total_days_volume

    
    @classmethod
    def total_volume_per_cow_per_day(cls, milking_date):
        """Get total volume of milk produced by each cow on a specific date."""
        return cls.objects.filter(milking_date=milking_date).values('cow').annotate(
            total_morning_volume=Sum('morning_volume'),
            total_evening_volume=Sum('evening_volume')
        )
    
    def clean(self):
        """Ensure only one milk production record exists per cow per day."""
        if Production.objects.filter(cow=self.cow, milking_date=self.milking_date).exclude(pk=self.pk).exists():
            raise ValidationError("A production record already exists for this cow on this date.")

    def save(self, *args, **kwargs):
        self.full_clean()  # Validate before saving
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Cow {self.cow.id_number} - Milking on {self.milking_date}"    

class Feeds(models.Model):
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
        indexes = [
            models.Index(fields=['date']),
            models.Index(fields=['feed_type']),
        ]

    def clean(self):
        # Ensure that the quantity of feed is always a positive number
        if self.quantity <= 0:
            raise ValidationError("Quantity must be a positive number.")

    def save(self, *args, **kwargs):
        self.full_clean()  # Validate before saving
        super(Feeds, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.feed_type.name} on {self.date} - {self.quantity} kg"
