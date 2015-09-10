from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import viewsets, views, status
from rest_framework.decorators import api_view

from polls.serializers import *


class ProjectSetView(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSrlzr
    
class EmployeeSetView(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSrlzr

class ProjectListView(views.APIView):
    def get(self, request, format=None):
        projects = Project.objects.all()
        serializer = ProjectSrlzr(projects, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProjectSrlzr(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectDetailView(views.APIView):
    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        project = self.get_object(pk)
        serializer = ProjectSrlzr(project)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        project = self.get_object(pk)
        serializer = ProjectSrlzr(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        project = self.get_object(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class EmployeeListView(views.APIView):
    def get(self, request, format=None):
        employees = Employee.objects.all()
        serializer = EmployeeSrlzr(employees, context={'request':request}, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EmployeeSrlzr(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeDetailView(views.APIView):
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        employee = self.get_object(pk)
        serializer = EmployeeSrlzr(employee)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        employee = self.get_object(pk)
        serializer = EmployeeSrlzr(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        employee = self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def index(request):
    return HttpResponse("Hello, world!")
