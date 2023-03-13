from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    name = forms.CharField(max_length=30, required=True)
    phone_number = forms.CharField(max_length=15, required=True)
    email = forms.EmailField(max_length=254, required=False)
    dob = forms.DateField(
        required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    address = forms.CharField(max_length=200, required=True)

    class Meta:
        model = User
        fields = ['name', 'phone_number',
                  'email', 'dob', 'address', 'password']
    widgets = {
        "password": forms.widgets.PasswordInput(attrs={"placeholder": "Enter strong password"}),
        "name": forms.widgets.TextInput(attrs={"placeholder": "Enter your name"}),
        "dob": forms.widgets.DateInput(attrs={"type": "date", "placeholder": "DD/MM/YYYY"}),
        "address": forms.widgets.TextInput(attrs={"placeholder": "Enter your address"}),
        "email": forms.widgets.EmailInput(attrs={"placeholder": "Enter your email(optional)", "required": False}),

    }
