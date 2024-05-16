from django.db import models
from inventory.models import Product


class FinancialTransaction(models.Model):
    TRANSACTION_TYPES = [
        ('EXPENSE', 'Expense'),
        ('REVENUE', 'Revenue'),
    ]

    date = models.DateField()
    transaction_type = models.CharField(max_length=7, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.transaction_type} - {self.amount} on {self.date}"

class Expense(models.Model):
    date = models.DateField()
    item = models.TextField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # Create a corresponding financial transaction
        super().save(*args, **kwargs)
        FinancialTransaction.objects.create(
            date=self.date,
            transaction_type='EXPENSE',
            amount=self.amount,
            description=self.description or f"Expense for item {self.item}"
        )

    def __str__(self):
        return f"Expense - {self.amount} on {self.date}"

class Revenue(models.Model):
    date = models.DateField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='revenues')
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    description = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # Calculate the total amount
        self.amount = self.quantity * self.unit_price
        super().save(*args, **kwargs)
        FinancialTransaction.objects.create(
            date=self.date,
            transaction_type='REVENUE',
            amount=self.amount,
            description=self.description or f"Revenue from {self.quantity} units of {self.product.name}"
        )

    def __str__(self):
        return f"Revenue - {self.amount} on {self.date}"
