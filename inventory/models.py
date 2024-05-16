from django.db import models

class Category(models.Model):
    CATEGORY_CHOICES = [
        ('CROP_HC', 'Crops (Human Consumption)'),
        ('CROP_LF', 'Crops (Livestock Feed)'),
        ('ANIMAL_PROD', 'Animal Products'),
        ('FARM_MACH', 'Farm Machinery'),
        ('TOOLS', 'Tools'),
        ('FERTILIZERS', 'Fertilizers'),
        ('PEST_HERB', 'Pesticides and Herbicides'),
        ('SEEDS', 'Seeds and Planting Materials'),
        ('ANIMAL_FEED', 'Animal Feed'),
        ('VET_SUPPLIES', 'Veterinary Supplies'),
        ('FARM_OPS', 'Farm Operations Supplies'),
        ('PACKAGING', 'Packaging Materials'),
        ('CONSTRUCTION', 'Construction Materials'),
        ('PROTECTIVE', 'Protective Gear'),
    ]

    name = models.CharField(max_length=50, choices=CATEGORY_CHOICES, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Inventory Category"
        verbose_name_plural = "Inventory Categories"

    def __str__(self):
        return self.get_name_display()
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    description = models.TextField(blank=True, null=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    sku = models.CharField(max_length=100, unique=True)  # Stock Keeping Unit
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Stock(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='stock')
    quantity = models.PositiveIntegerField(default=0)
    minimum_required = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"
    
    def check_stock_level(self):
        return self.quantity < self.minimum_required

class Transaction(models.Model):
    
    TRANSACTION_TYPES = [
        ('IN', 'Stock In'),
        ('OUT', 'Stock Out'),
        ('ADJ', 'Adjustment'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='transactions')
    transaction_type = models.CharField(max_length=3, choices=TRANSACTION_TYPES)
    quantity = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.product.name} - {self.transaction_type} - {self.quantity}"