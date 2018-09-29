# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect, render
from django.contrib import auth
from django.template.context_processors import csrf


# Create your views here.
def login(request):

    if request.POST:
        # this two variables for internal purpose only (only this template)
        # that does not mean username of authenticated user
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            return render(request, 'login.html', {'login_error': 'Пользователь не найден',
                                                  "username": username,
                                                  "password": password})
    else:  # means GET request (form does not send)
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect("/")
