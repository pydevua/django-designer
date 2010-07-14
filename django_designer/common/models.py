from django.db import models
from django_code.applications import init_django_project
from managers import AppManager

class Project(models.Model):
    "Django project"
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    
    def __unicode__(self):
        return self.name


class Application(models.Model):
    "Django application"
    name = models.CharField(max_length=150)
    project = models.ForeignKey(Project, related_name='applications')
    description = models.TextField(null=True, blank=True)
    
    package = models.CharField(max_length=250, null=True, blank=True)
    
    is_external = models.BooleanField(default=False)
    is_django = models.BooleanField(default=False)
    
    objects = AppManager()
    
    class Meta:
        unique_together = ('name', 'project')
    
    def __unicode__(self):
        return self.name



def on_project_save(instance, *args, **kwargs):
    if kwargs['created']:
        init_django_project(instance)

models.signals.post_save.connect(on_project_save, sender=Project)
