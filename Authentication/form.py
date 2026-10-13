from django import forms
from django.contrib.auth.hashers import make_password, check_password
from UserApp.models import *
import re

from UserApp.models import *


class SignupFrom(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    bio = forms.CharField(max_length=1500)
    email = forms.EmailField()
    phone = forms.CharField(max_length=20)
    password = forms.CharField(max_length=300)
    confirm_password = forms.CharField(max_length=300)
    circle_image = forms.ImageField(required=False)
    rectangle_image = forms.ImageField(required=False)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
        if not re.fullmatch(pattern, password):
            raise forms.ValidationError("Passwords is not strong enough.")

        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        similar_username = User.objects.filter(username=username)
        if similar_username.exists():
            raise forms.ValidationError("Username already exists")
        similar_email = User.objects.filter(email=email)
        if similar_email.exists():
            raise forms.ValidationError("Email already exists")
        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=50)

    def clean(self):
        clean_data = super().clean()
        password = clean_data.get("password")
        username = clean_data.get("username")
        try:
            target_user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError("Username does not exist")
        if not check_password(password, target_user.password):
            raise forms.ValidationError("Password does not match")
        return clean_data

