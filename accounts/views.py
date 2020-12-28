from .models import *
from django.contrib import messages
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from .forms import CreateUserForm, CreateCustomerForm
from .decorators import unauthenticated_user, admin_only
from django.contrib.auth import authenticate, login, logout


def home(request):
    form = CreateCustomerForm()
    if request.method == 'POST':
        form = CreateCustomerForm(request.POST)
        if form.is_valid():
            form.save()
            customer = form.cleaned_data.get('phone_number')
            messages.success(request, 'Order was created for ' + customer)
            return redirect('home')
        else:
            messages.info(request, 'Phone number and Destination are required fields')
    return render(request, 'accounts/home.html', {'form': form})


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.info(request, 'Username or Password is incorrect')
        else:
            login(request, user)
            if request.user.is_staff:
                return redirect('administrator')
            else:
                return redirect('home')
    return render(request, 'accounts/login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')


def registrationPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    return render(request, 'accounts/registration.html', {'form': form})


@admin_only
def administratorPage(request):
    customers = Customer.objects.all()
    return render(request, 'accounts/administrator.html', {'customers': customers})
