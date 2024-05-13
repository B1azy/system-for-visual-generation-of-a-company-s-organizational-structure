from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)

class SubDivision(models.Model):
    name = models.CharField(max_length=100)
    LocationID = models.ForeignKey(Location, null=False, on_delete=models.CASCADE)

class Division(models.Model):
    name = models.CharField(max_length=100)
    SubDivisionID = models.ForeignKey(SubDivision, null=False, on_delete=models.CASCADE)

class Group(models.Model):
    name = models.CharField(max_length=100)
    DivisionID = models.ForeignKey(Division, null=False, on_delete=models.CASCADE)

class Person(models.Model):
    name = models.CharField(max_length=100)
    GroupID = models.ForeignKey(Group, null=False, on_delete=models.CASCADE)
    WorkType = models.CharField(max_length=100)
    Post = models.CharField(max_length=100)

class Persons(models.Model):
    Number = models.CharField(max_length=10, null=True)
    Fase = models.CharField(max_length=100, null=True)
    LocationName = models.CharField(max_length=100, null=True)
    SubDivisionName = models.CharField(max_length=100, null=True)
    DivisionName = models.CharField(max_length=100, null=True)
    GroupName = models.CharField(max_length=100, null=True)
    Post = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=100, null=True)
    WorkType = models.CharField(max_length=100, null=True)


