from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from utils.views import render_to, render_json
from common.models import Application
from model_editor.models import Model
from model_editor.forms import NewModelForm, EditModelForm, ModelFieldFormSet
from forms import ApplicationForm



#TODO: get_object_or_404 in ajax views shold be replaced with some other solution

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


@render_to('model_editor/models.html')
def model_list(request, app_id):
    application = get_object_or_404(Application, pk=app_id)
    return {'application': application}


@render_json
def new_model(request, app_id):
    application = get_object_or_404(Application, pk=app_id)
    form = NewModelForm(request.POST, application)
    if form.is_valid():
        model = form.save()
        return {'success':True, 'url': reverse('edit-model', args=[model.pk])}
    else:
        return {'success':False, 'error': unicode(form.errors)}

@render_to('model_editor/edit.html') #TODO: think of template namings
def edit_model(request, model_id):
    model = get_object_or_404(Model, pk=model_id)
    if request.method == 'POST':
        form = EditModelForm(request.POST, instance=model)
        field_formset = ModelFieldFormSet(request.POST, prefix='fields')
        if form.is_valid():
            form.save() #TODO: show message (messages should be with growl? but done with django-messages)
        if field_formset.is_valid():
            fields = field_formset.save(commit=False)
            for field in fields:
                field.model = model
                field.save()
            field_formset = ModelFieldFormSet(queryset=model.field_set.all(), prefix='fields')
    else:
        form = EditModelForm(instance=model)
        field_formset = ModelFieldFormSet(queryset=model.field_set.all(), prefix='fields')
    return {'form': form, 'field_formset': field_formset, 'model':model}
