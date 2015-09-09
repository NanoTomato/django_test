from django.contrib import admin

from .models import Project, Employee

class IEmployee(admin.ModelAdmin):
    list_display = ("name", "birthdate", "project")
    list_filter = ["project"]


admin.site.register(Project)
admin.site.register(Employee, IEmployee)

