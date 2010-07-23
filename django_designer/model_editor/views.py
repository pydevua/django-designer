from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.core.urlresolvers import reverse
from utils.views import render_to, JSONResponse, render_json
from codegenerator.models import model_code, app_models_code
from common.models import Application
from models import Model, UniqueTogether
from forms import UniqueTogetherForm, NewModelForm, EditModelForm, ModelFieldFormSet


#TODO: get_object_or_404 in ajax views should be replaced with some other solution

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


def delete_model(request, model_id):
    model = get_object_or_404(Model, pk=model_id)
    model.delete()
    return JSONResponse({'success': True})


def _code_response(code):
    return HttpResponse('<div style="width: 500px; height: 400px;"><textarea style="width: 450px; height: 350px;">%s</textarea></div>' % code)

def get_models_code(request, model_id):
    model = get_object_or_404(Model, pk=model_id)
    code = model_code(model)
    return _code_response('\n'.join(code.lines()))


def get_app_models_code(request, app_id):
    app = get_object_or_404(Application, pk=app_id)
    code = app_models_code(app)
    return _code_response(code)


@render_to('model_editor/unique_together_add.html')
def unique_together_add(request, model_id):
    model = get_object_or_404(Model, pk=model_id)
    if request.method == 'POST':
        form = UniqueTogetherForm(request.POST, model=model)
        if form.is_valid():
            form.save()
            html = render_to_string('model_editor/unique_together_list.html', {'model': model})
            return JSONResponse({'html':html})
        return JSONResponse({'error': form.errors['fields']})
    else:
        form = UniqueTogetherForm(model=model)
    return {'form':form}


@render_to('model_editor/unique_together_list.html')
def unique_together_remove(request, id):
    ut = get_object_or_404(UniqueTogether, pk=id)
    model = ut.model
    ut.delete()
    return {'model': model}
