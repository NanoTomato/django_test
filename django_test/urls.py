from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers

from polls import views


router = routers.DefaultRouter()
router.register(r'projects', views.ProjectSetView)
router.register(r'employee', views.EmployeeSetView)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api_auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
)
