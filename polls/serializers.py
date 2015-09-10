from polls.models import Project, Employee

from rest_framework import serializers

class ProjectSrlzr(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('name',)

class EmployeeSrlzr(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ('name', 'birthdate', 'project')
