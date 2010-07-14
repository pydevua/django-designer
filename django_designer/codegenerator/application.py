import logging
from models import app_models_code
#from forms import forms_code
#from admin import admin_code
#from urls import app_urls

logger = logging.getLogger('BuildLogger')

def build_application(application, project_package):
    if not application.is_external:
        package = project_package.child_package(application.name)
        #package.write_module('urls', app_urls(application))
        package.write_module('models', app_models_code(application))
#        package.write_module('forms', forms_code(application))
#        package.write_module('admin', admin_code(application))
