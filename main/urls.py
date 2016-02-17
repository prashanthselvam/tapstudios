from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^projects/$', views.projects, name='projects'),
    url(r'^projects/(?P<slug>[-\w]+)/$', views.project_detail, name='project_detail'),
]