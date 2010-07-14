from utils.views import render_to
from models import Project
from forms import ProjectForm
from django.shortcuts import redirect

def _pick_project(request, project):
    "Picking project and redirecting to manage it"
    proj_pk = isinstance(project, Project) and project.pk or int(project)
    request.session['CURRENT_PROJECT'] = proj_pk
    return redirect('main')


@render_to('projects/manage.html')
def manage_projects(request):
    if 'pick' in request.GET:
        return _pick_project(request, request.GET['pick'])
    
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save()
            return _pick_project(request, project)
    else:
        form = ProjectForm()
    return {'projects': Project.objects.all(), 'form': form}
