# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import HomeForm


# Create your views here.
def home(request):
    if request.method == 'POST':
        form = HomeForm(request.POST)
        if form.is_valid():
            Name = form.cleaned_data.get('Name', None)
            SSN = form.cleaned_data.get('SSN', None)
            print('Name:'+ Name,'SSN:'+ SSN)
            validate(Name,SSN)

    name = "Welcome"
    return render(request, "home.html", {"name": name})


def valid(request):
    return render(request, "Validated.html", {})


def Diag(request):
    return render(request, "Diag.html", {})


def validate(n, s):
    if n == "Lokesh":
        if s == 1234:
            redirect(valid())
    else:
        redirect(Diag())


