from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'projects/$', views.ProjectListView.as_view()),
    url(r'projects/(?P<pk>[0-9]+)$', views.ProjectDetailView.as_view()),
    url(r'employee/$', views.EmployeeListView.as_view()),
    url(r'employee/(?P<pk>[0-9]+)$', views.EmployeeDetailView.as_view()),
]
