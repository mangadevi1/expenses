from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Category, Transaction,Loan
from .forms import TransactionForm


# Home page
def index(request):
    return render(request, 'index.html')

# Login page
def login(request):
    return render(request, 'login.html')


def transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transaction')
    else:
        form = TransactionForm()

    transactions = Transaction.objects.all().order_by('-date')
    context = {
        'transactions': transactions,
        'form': form,
    }
    return render(request, 'transection.html', context)

# Register page
def register(request):
    if request.method == "POST":
        # Handle form submission logic here
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Password check
        if password != confirm_password:
           
            return redirect('register')

        # Check if username already exists
        if User.objects.filter(username=username).exists():
           
            return redirect('register')

        # Create new user
        User.objects.create_user(username=username, email=email, password=password)
      
        return redirect('login')
    

    # GET request → render registration page
    return render(request, 'register.html')
def loan_list_create_view(request):
    loans = Loan.objects.all()
    # For now, just render loans list, add form processing later
    return render(request, 'loans.html', {'loans': loans})
def categories(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description', '')

        # Avoid duplicate category names
        if not Category.objects.filter(name=name).exists():
            Category.objects.create(name=name, description=description)

        return redirect('categories')  # Redirect after form submit

    # GET request: show all categories
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories}) 