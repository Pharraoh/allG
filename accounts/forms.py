# myapp/forms.py
from django import forms

class MyCustomForm(forms.Form):
    # Define your form fields here
    # firstname = forms.CharField(label='Firstname', max_length=100)
    # lastname = forms.CharField(label='Lastname', max_length=100)
    username = forms.CharField(label='Username', max_length=100)
    # email = forms.EmailField(label='Email')
    # age = forms.CharField(label='age', max_length=3)
    password = forms.CharField(label='Password')
    # Add more fields as needed
