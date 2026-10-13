from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from UserApp.models import *
from .form import *

def signup_view(request):
    if request.method == 'POST':
        form = SignupFrom(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            User.objects.create(
                first_name=data['first_name'],
                last_name=data['last_name'],
                username=data['username'],
                bio=data['bio'],
                email=data['email'],
                phone=data['phone'],
                password=make_password(data['password']),
                circle_image=data['circle_image'],
                rectangle_image=data['rectangle_image'],
            )
            return redirect('login')
        else:
            return render(request, "signup.html", {'error' : 'wrong information'})
    return render(request, "signup.html")


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            request.session['user_id'] = User.objects.get(username=data['username']).id
            return redirect('profile', user_id = User.objects.get(username=data['username']).id)
        else:
            return redirect('login')
    return render(request, "login.html")

def logout_view(request):
    request.session.flush()
    return redirect('login')