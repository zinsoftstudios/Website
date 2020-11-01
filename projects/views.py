from django.shortcuts import render
from projects.models import Projects

# Create your views here.

def project_index(request):
    projects = Projects.objects.all()
    context = {
            'projects': projects
        }
    return render(request, 'project_index.html', context)

def project_details(request, pk):
    project = Projects.objects.get(pk = pk)
    context = {
            'project': project
        }
    return render(request, 'project_details.html', context)