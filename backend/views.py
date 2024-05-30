from rest_framework.decorators import APIView
from rest_framework.response import Response
from django.shortcuts import render, redirect
from .models import Location, SubDivision, Division,Group,Person
from .serializer import LocationsSerializer,SubDivisionSerializer,DivisionSerializer,GroupSerializer,PersonSerializer



class index(APIView):
    def get(self,request):
        return Response(request, 'index.html',{'dop': (LocationsSerializer(Location.objects.all(), many = True).data,
                                                                            SubDivisionSerializer(SubDivision.objects.all(), many = True).data,
                                                                            DivisionSerializer(Division.objects.all(), many = True).data,
                                                                            GroupSerializer(Group.objects.all(), many = True).data,
                                                                            PersonSerializer(Person.objects.all(), many = True).data)})