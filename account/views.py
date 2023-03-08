"""
This module contains views for user registration and login pages.
Functions:
- logout_view: Logs out the current user and redirects to the homepage.
- login_view: Renders the login form and handles user authentication.
- registration_view: Renders the registration form and creates a new user.
Dependencies:
- render: Renders an HTML template with a given context dictionary.
- redirect: Redirects to a given URL.
- get_common_context: A function from the main_page.context_data module that returns a dictionary with common
context data for all pages.
- UserRegistration: A Django form class for user registration.
- UserLogin: A Django form class for user login.
- authenticate: Authenticates a user with a given username and password.
- login: Logs in a user and creates a session.
- logout: Logs out the current user and destroys the session.
- User: The Django user model for the application.
"""

from django.shortcuts import render, redirect
from main_page.context_data import get_common_context
from .forms import UserRegistration, UserLogin
from django.contrib.auth import login, authenticate, logout


def logout_view(request):
    logout(request)
    return redirect('/')

def login_view(request):
    form = UserLogin(request.POST or None)
    next_get = request.GET.get('next')
    user_manager = request.user.groups.filter(name='manager').exists()
    user_auth = request.user.is_authenticated

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)

        next_post = request.POST.get('next')
        return redirect(next_get or next_post or '/')

    data = {
        'form': form,
        'user_manager': user_manager,
        'user_auth': user_auth,
    }
    context_data = get_common_context()
    data.update(context_data)
    return render(request, 'login.html', context=data)

def registration_view(request):
    form = UserRegistration(request.POST or None)
    user_manager = request.user.groups.filter(name='manager').exists()
    user_auth = request.user.is_authenticated
    context_data = get_common_context()

    if form.is_valid():
        new_user = form.save(commit=False)
        new_user.set_password(form.cleaned_data['password'])
        new_user.save()
        data = {
            'form': form,
            'user_manager': user_manager,
            'user_auth': user_auth,
            'user': new_user,
        }
        data.update(context_data)
        return render(request, 'registration_done.html', context=data)

    data = {
        'form': form,
        'user_manager': user_manager,
        'user_auth': user_auth,
    }
    data.update(context_data)
    return render(request, 'registration.html', context=data)