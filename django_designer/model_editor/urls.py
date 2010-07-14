from django.conf.urls.defaults import *

urlpatterns = patterns('model_editor.views',
    url(r'^model-code/(\d+)/$', 'get_models_code', name='model-code'),
    url(r'^app-code/(\d+)/$', 'get_app_models_code', name='app-models-code'),
)
