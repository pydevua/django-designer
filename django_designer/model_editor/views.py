from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponse
from utils.views import render_to, JSONResponse
from codegenerator.models import model_code, app_models_code
from common.models import Application
from models import Model, UniqueTogether
from forms import UniqueTogetherForm
from django.template.loader import render_to_string


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
