# finance/forms.py

from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['type', 'amount', 'currency', 'description', 'date', 'category', 'payment_method']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
