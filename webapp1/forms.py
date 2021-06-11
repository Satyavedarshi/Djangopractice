
from django import forms

class InputForm(forms.Form):
    firstname = forms.CharField(max_length=200)
    lastname = forms.CharField(max_length=200)
    roll_number = forms.IntegerField(help_text='Enter your 6 digit Roll Number ')
    password = forms.CharField(widget=forms.PasswordInput())