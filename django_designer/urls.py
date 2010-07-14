from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^projects/$', 'common.views.manage_projects', name='manage-projects'),
    url(r'^designer/$', 'ui.views.main', name='main'),
    url(r'^designer/application-add/$', 'ui.views.ajax_add_application', name='application-add'),
    url(r'^designer/models/(\d+)/$', 'ui.views.model_list', name='application-models'),
    url(r'^designer/new-model/(\d+)/$', 'ui.views.new_model', name='new-model'),
    url(r'^designer/edit-model/(\d+)/$', 'ui.views.edit_model', name='edit-model'),
    
    ('^designer/models/', include('model_editor.urls')),

    
    (r'^admin/', include(admin.site.urls)),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
