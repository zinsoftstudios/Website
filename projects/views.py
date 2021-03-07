from django.shortcuts import render
from projects.models import Projects
from datetime import datetime

# Create your views here.

def project_index(request):
    projects = Projects.objects.all()
    context = {
            'projects': projects,
            'year':datetime.now().year,
        }
    return render(request, 'project_index.html', context)

def project_details(request, pk):
    project = Projects.objects.get(pk = pk)
    context = {
            'project': project,
            'year':datetime.now().year,
        }
    return render(request, 'project_details.html', context)