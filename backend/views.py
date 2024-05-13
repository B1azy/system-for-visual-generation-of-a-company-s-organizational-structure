from django.shortcuts import render, redirect
from .models import Location, SubDivision, Division



def index(request):
    return render(request, 'index.html')