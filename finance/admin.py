from django.contrib import admin
from .models import FinancialTransaction, Revenue, Expense
# Register your models here.
admin.site.register(FinancialTransaction)
admin.site.register(Revenue)
admin.site.register(Expense)
