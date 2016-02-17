from django.shortcuts import render, get_object_or_404
from .models import Project, ProjectImages

# Create your views here.

def index(request):
    return render(request, 'main/index.html', {})

def about(request):
	return render(request, 'main/about.html', {})

def projects(request):
	projects_list = Project.objects.all()
	return render(request, 'main/projects.html', {'projects_list': projects_list})

def project_detail(request, slug):
	project = get_object_or_404(Project, slug=slug)
	return render(request, 'main/project_detail.html', {'project':project, 'images': ProjectImages})	