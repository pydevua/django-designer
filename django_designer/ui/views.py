from django.http import HttpResponse
from utils.views import render_to
from forms import ApplicationForm


@render_to('designer.html')
def main(request):
    return {}

@render_to('applications.html')
def ajax_add_application(request): #TODO: ajax prefix not needed
    form = ApplicationForm(request.POST, request.project)
    if form.is_valid():
        form.save()
        return {}
    return HttpResponse(unicode(form.errors))
