from django.contrib import admin

# Register your models here.
from .models import Category, Product, Stock, Transaction

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Stock)
admin.site.register(Transaction)
# admin.site.register()