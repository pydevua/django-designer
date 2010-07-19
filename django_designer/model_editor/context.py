from models import Model

def project_models(request):
    if hasattr(request, 'project'):
        queryset = Model.objects.filter(application__project=request.project)
        return {'MODELS': [{'pk': i.pk, 'name': unicode(i)} for i in queryset]}
    return {}