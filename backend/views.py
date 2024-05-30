from django.shortcuts import render, redirect
from .models import Location, SubDivision, Division
from .serializer import LocationsSerializer



def index(request):

    return render(request, 'index.html',{'dop': LocationsSerializer(Location.objects.get(id = 1))})