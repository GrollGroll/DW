from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth

from users.forms import UserLoginForm, UserRegisrtationForm
from django.urls import reverse


def login(request):
    if request.method == 'POST':
        form = UserLoginForm (data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect('/')
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/authentication.html', context)


def registration(request):
    error = None
    if request.method == 'POST':
        form = UserRegisrtationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect(reverse('authentication'))
        else:
            error = form.errors
            print(error)
    else:
        form = UserRegisrtationForm()
    context = {'form': form, 'Error':error}
    return render(request, 'users/registration.html', context)

