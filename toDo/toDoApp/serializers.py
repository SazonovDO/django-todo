from rest_framework import serializers
from .models import toDoList, company

class toDoListSerializers(serializers.ModelSerializer):
    class Meta:
        model = toDoList
        fields = ('id', 'name', 'details', 'company', 'finished')

class companySerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = company
        fields = ('id', 'url', 'name')


