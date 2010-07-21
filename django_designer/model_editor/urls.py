from django.conf.urls.defaults import *

urlpatterns = patterns('model_editor.views',
    url(r'^model-code/(\d+)/$', 'get_models_code', name='model-code'),
    url(r'^app-code/(\d+)/$', 'get_app_models_code', name='app-models-code'),
    url(r'^unique-together-add/(\d+)/$', 'unique_together_add', name='unique-together-add'),
    url(r'^unique-together-remove/(\d+)/$', 'unique_together_remove', name='unique-together-remove'),
)
