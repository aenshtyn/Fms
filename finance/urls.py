# finance/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TransactionViewSet, BudgetViewSet, ExpenseViewSet, IncomeViewSet, InvoiceViewSet, PaymentViewSet, AccountViewSet, TaxViewSet, AssetViewSet, LiabilityViewSet, FinancialReportViewSet, ExpenseCategoryViewSet, IncomeCategoryViewSet, LoanViewSet, InvestmentViewSet, InterestViewSet, CreditViewSet, FinancialGoalViewSet, FinancialForecastViewSet, FinancialInstitutionViewSet, ExpenseApprovalViewSet, CategorizationViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'transactions', TransactionViewSet, basename='transactions')
router.register(r'budgets', BudgetViewSet, basename='budgets')
router.register(r'expenses', ExpenseViewSet, basename='expenses')
router.register(r'incomes', IncomeViewSet, basename='incomes')
router.register(r'invoices', InvoiceViewSet, basename='invoices')
router.register(r'payments', PaymentViewSet, basename='payments')
router.register(r'accounts', AccountViewSet, basename='accounts')
router.register(r'taxes', TaxViewSet, basename='taxes')
router.register(r'assets', AssetViewSet, basename='assets')
router.register(r'liabilities', LiabilityViewSet, basename='liabilities')
router.register(r'financial-reports', FinancialReportViewSet, basename='financial_reports')
router.register(r'expense-categories', ExpenseCategoryViewSet, basename='expense_categories')
router.register(r'income-categories', IncomeCategoryViewSet, basename='income_categories')
router.register(r'loans', LoanViewSet, basename='loans')
router.register(r'investments', InvestmentViewSet, basename='investments')
router.register(r'interests', InterestViewSet, basename='interests')
router.register(r'credits', CreditViewSet, basename='credits')
router.register(r'financial-goals', FinancialGoalViewSet, basename='financial_goals')
router.register(r'financial-forecasts', FinancialForecastViewSet, basename='financial_forecasts')
router.register(r'financial-institutions', FinancialInstitutionViewSet, basename='financial_institutions')
router.register(r'expense-approvals', ExpenseApprovalViewSet, basename='expense_approvals')
router.register(r'categorizations', CategorizationViewSet, basename='categorizations')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
