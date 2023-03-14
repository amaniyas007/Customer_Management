from django import forms
from django.forms import TextInput, Select, DateInput, BooleanField, Textarea

from posts.models import Customer, Event


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

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = "__all__"

        widgets = {
            'title': TextInput(attrs={'class':'required input'}),
            'event_type': Select(attrs={'class':'required input'},choices=Event.CHOICES),
            'event_date': DateInput(attrs={'class':'required input', 'type':'date'}, format="%Y-%m-%dT%H:%M"),
        }