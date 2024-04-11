from django.contrib import admin

from .models import Account, Payment, Liability, Asset, Credit, Categorization,Income, IncomeCategory, Loan, Investment, Salary, FinancialForecast, FinancialGoal, Expense, ExpenseApproval, ExpenseCategory, Budget, Interest, Invoice 
# Register your models here.
admin.site.register(Income)
admin.site.register(Invoice)
admin.site.register(IncomeCategory)
admin.site.register(Loan)
# admin.site.register(IncomeCategory)
admin.site.register(Investment)
admin.site.register(FinancialForecast)
admin.site.register(FinancialGoal)
admin.site.register(Expense)
admin.site.register(ExpenseApproval)
admin.site.register(ExpenseCategory)
admin.site.register(Budget)
admin.site.register(Salary)
admin.site.register(Interest)
admin.site.register(Account)
admin.site.register(Payment)
admin.site.register(Liability)
admin.site.register(Asset)
admin.site.register(Credit)
admin.site.register(Categorization)