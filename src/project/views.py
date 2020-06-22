from django.shortcuts import render,HttpResponse
from project.models import Project


# Create your views here.
def index(request):
    if request.method == 'GET':
        Projects = Project.objects.all()

    return render(request, 'project/home.html', {'projects' : Projects})
    


