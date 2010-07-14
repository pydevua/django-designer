import logging
import os
import shutil
from tools import Package
from application import build_application

def rel(*x):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)

def write_file(path, content):
    dir_path = os.path.dirname(path)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    open(path, 'w').write(content)

logger = logging.getLogger('BuildLogger')


def build_project(project, path):
    from django.conf import settings
    package = Package(os.path.join(path, project.name))
    #package.write_module('settings', get_settings(project))
    #package.write_module('urls', project_urls(project))
    package.copy(os.path.join(settings.BASE_PATH, 'manage.py'), 'manage.py')

    for app in project.application_set.all():
        build_application(app, package)
