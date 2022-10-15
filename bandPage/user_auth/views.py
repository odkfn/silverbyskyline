from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from user_auth.forms import SignUpForm

# Create your views here.

def login_user(request):
    return render(request, 'registration/login.html')

# Old placeholder register method superseded below
# def register(request):
#    return HttpResponse("Welcome to the registration page.")

# Followed this tutorial on how to make a register page with custom inputs:
# https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html#sign-up-with-extra-fields
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request,user)
            return redirect('silverbyskyline:silverbyskyline')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})
