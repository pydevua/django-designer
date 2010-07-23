from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

def redirect2projects(request):
    from django.http import HttpResponseRedirect
    return HttpResponseRedirect('/projects/')

urlpatterns = patterns('',
    (r'^$', redirect2projects),
    url(r'^projects/$', 'common.views.manage_projects', name='manage-projects'),
    url(r'^designer/$', 'ui.views.main', name='main'),
    url(r'^designer/application-add/$', 'ui.views.ajax_add_application', name='application-add'),
    ('^designer/models/', include('model_editor.urls')),

    
    (r'^admin/', include(admin.site.urls)),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
