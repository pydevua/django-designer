from common.models import Project
from django.shortcuts import redirect


class ProjectMiddleware(object):
    """
    Stores current project in request object
    makes redirect if project not set
    """
    def process_request(self, request):
        if request.session.get('CURRENT_PROJECT'):
            request.project = Project.objects.get(pk=request.session['CURRENT_PROJECT'])
            #TODO: make it lazy ^
            return
        if request.path.startswith('/designer/'):
            return redirect('manage-projects')
        