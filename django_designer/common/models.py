from django.db import models

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
    
    is_external = models.BooleanField(default=False)
    is_django = models.BooleanField(default=False)
    
    class Meta:
        unique_together = ('name', 'project')
    
    def __unicode__(self):
        return self.name
