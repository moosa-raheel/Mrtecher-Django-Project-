from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# User Registration Form 
class Registration(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(),error_messages={"required":"Please enter password"},label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput(),error_messages={"required":"Please re-enter password"}, label="Confirm password")
    class Meta:
        model = User
        fields = ("first_name","last_name","username","email")
        error_messages = {"username":{"required":"Please enter username"}}