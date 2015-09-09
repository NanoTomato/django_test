from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=30)
    birthdate = models.DateField()
    project = models.ForeignKey(Project)

    def __unicode__(self):
        return self.name
