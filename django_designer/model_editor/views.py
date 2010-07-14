from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from models import Model
from codegenerator.models import model_code, app_models_code
from common.models import Application



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
