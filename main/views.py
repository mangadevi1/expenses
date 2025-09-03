from django.shortcuts import render, redirect
from django.contrib.auth.models import User


# Home page
def index(request):
    return render(request, 'index.html')

# Login page
def login(request):
    return render(request, 'login.html')
def transection(request):
    return render(request, 'transection.html')

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

