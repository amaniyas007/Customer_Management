from django import forms
from django.forms import TextInput, Select, DateInput, BooleanField, Textarea

from posts.models import Customer


class CustomerForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': "form-control", "type": "text", "placeholder": "Enter Username"}))
    password = forms.CharField(widget=forms.TextInput(
        attrs={'class': "form-control", "type": "password", "placeholder": "Enter your Password"}))

    class Meta:
        model = Customer
        exclude = ('user', 'is_deleted')

        widgets = {
            'first_name': TextInput(attrs={'class': "form-control", "type": "text", "placeholder": "Enter your first name"}),
            'last_name': TextInput(attrs={'class': "form-control", "type": "text", "placeholder": "Enter your last name"}),
            'phone_no': TextInput(attrs={'class': "form-control", "type": "number", "placeholder": "Enter your phone number"}),
            'name': TextInput(attrs={'class': "form-control", "type": "text"}),
            'email': TextInput(attrs={'class': "form-control", "type": "email", "placeholder": "Enter your Email Id", "required": "False"}),
            'address': Textarea(attrs={'class': "form-control", 'rows': 5, "cols": "47", "type": "text", "placeholder": "Enter your Adress"}),
            'date_of_birth': DateInput(attrs={'class': "form-control", "type": "date", 'style': "background:#fff;color:#000"}),

        }
