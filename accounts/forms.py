from .models import Customer
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CreateCustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['phone_number', 'destination']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
