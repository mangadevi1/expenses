from django.contrib import admin
from .models import Transaction, Loan, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description")
    search_fields = ("name","id")


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("id", "type", "amount", "currency", "date", "payment_method", "category")
    list_filter = ("type", "currency", "payment_method", "date")
    search_fields = ("description",)
    date_hierarchy = "date"


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "lender", "loan_type", "start_date", "tenure", "interest_rate", "amount", "status")
    list_filter = ("loan_type", "status", "start_date")
    search_fields = ("name", "lender")
