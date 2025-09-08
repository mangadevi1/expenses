from django.db import models
# from django.utils import timezone

# ✅ Categories Model
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.description}"


# ✅ Transactions Model
class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]
    PAYMENT_METHODS = [
        ('cash', 'Cash'),
        ('card', 'Card'),
        ('bank', 'Bank Transfer'),
        ('upi', 'UPI'),
        ('other', 'Other'),
    ]

    type = models.CharField(max_length=10, choices=TRANSACTION_TYPES, default='expense')  # Add a default here
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=10, default="INR")
    description = models.TextField(blank=True, null=True)
    date = models.DateField()
    timestamp = models.DateTimeField(auto_now=True) # Add default=now here temporarily
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS, default="cash")


# ✅ Loans Model
class Loan(models.Model):
    LOAN_TYPES = [
        ('personal', 'Personal'),
        ('home', 'Home'),
        ('car', 'Car'),
        ('education', 'Education'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    lender = models.CharField(max_length=100)
    loan_type = models.CharField(max_length=20, choices=LOAN_TYPES)
    start_date = models.DateField()
    tenure = models.PositiveIntegerField(help_text="Tenure in months")
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2, help_text="Interest rate %")
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    emi_amount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    balance = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=10, choices=[('active', 'Active'), ('closed', 'Closed')], default="active")
    description = models.TextField(blank=True, null=True)
    recurring = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.lender})"

