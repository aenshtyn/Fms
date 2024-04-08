# finance/views.py
from rest_framework import viewsets
from .models import Transaction, Budget, Expense, Income, Invoice, Payment, Account, Tax, Asset, Liability, FinancialReport, ExpenseCategory, IncomeCategory, Loan, Investment, Interest, Credit, FinancialGoal, FinancialForecast, FinancialInstitution, ExpenseApproval, Categorization
from .serializers import TransactionSerializer, BudgetSerializer, ExpenseSerializer, IncomeSerializer, InvoiceSerializer, PaymentSerializer, AccountSerializer, TaxSerializer, AssetSerializer, LiabilitySerializer, FinancialReportSerializer, ExpenseCategorySerializer, IncomeCategorySerializer, LoanSerializer, InvestmentSerializer, InterestSerializer, CreditSerializer, FinancialGoalSerializer, FinancialForecastSerializer, FinancialInstitutionSerializer, ExpenseApprovalSerializer, CategorizationSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class BudgetViewSet(viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class IncomeViewSet(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class TaxViewSet(viewsets.ModelViewSet):
    queryset = Tax.objects.all()
    serializer_class = TaxSerializer

class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

class LiabilityViewSet(viewsets.ModelViewSet):
    queryset = Liability.objects.all()
    serializer_class = LiabilitySerializer

class FinancialReportViewSet(viewsets.ModelViewSet):
    queryset = FinancialReport.objects.all()
    serializer_class = FinancialReportSerializer

class ExpenseCategoryViewSet(viewsets.ModelViewSet):
    queryset = ExpenseCategory.objects.all()
    serializer_class = ExpenseCategorySerializer

class IncomeCategoryViewSet(viewsets.ModelViewSet):
    queryset = IncomeCategory.objects.all()
    serializer_class = IncomeCategorySerializer

class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

class InvestmentViewSet(viewsets.ModelViewSet):
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer

class InterestViewSet(viewsets.ModelViewSet):
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer

class CreditViewSet(viewsets.ModelViewSet):
    queryset = Credit.objects.all()
    serializer_class = CreditSerializer

class FinancialGoalViewSet(viewsets.ModelViewSet):
    queryset = FinancialGoal.objects.all()
    serializer_class = FinancialGoalSerializer

class FinancialForecastViewSet(viewsets.ModelViewSet):
    queryset = FinancialForecast.objects.all()
    serializer_class = FinancialForecastSerializer

class FinancialInstitutionViewSet(viewsets.ModelViewSet):
    queryset = FinancialInstitution.objects.all()
    serializer_class = FinancialInstitutionSerializer

class ExpenseApprovalViewSet(viewsets.ModelViewSet):
    queryset = ExpenseApproval.objects.all()
    serializer_class = ExpenseApprovalSerializer

class CategorizationViewSet(viewsets.ModelViewSet):
    queryset = Categorization.objects.all()
    serializer_class = CategorizationSerializer
