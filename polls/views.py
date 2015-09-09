from django.http import HttpResponse
from rest_framework import viewsets

from polls.serializers import *


class ProjectSetView(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSrlzr
    
class EmployeeSetView(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSzlzr

def index(request):
    return HttpResponse("Hello, world!")
