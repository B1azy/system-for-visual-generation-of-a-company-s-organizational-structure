from rest_framework.serializers import ModelSerializer
from .models import Location,SubDivision,Division,Group,Person
class LocationsSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields ='__all__'

class SubDivisionSerializer(ModelSerializer):
    class Meta:
        model = SubDivision
        fields ='__all__'

class DivisionSerializer(ModelSerializer):
    class Meta:
        model = Division
        fields ='__all__'

class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields ='__all__'

class PersonSerializer(ModelSerializer):
    class Meta:
        model = Person
        fields ='__all__'
