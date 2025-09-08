from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('login/',views.login, name='login'),
    path('register/',views.register,name="register"),
    path("transactions/",views.transaction,name="transaction"),
    path("loans/",views.loan_list_create_view,name="loans"),
    path("categories/",views.categories,name="categories")  
]
