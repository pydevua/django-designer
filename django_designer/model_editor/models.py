from django.db import models
from common.models import Application
from utils.models import SortableModel

class Model(models.Model):
    "Django model"
    name = models.CharField(max_length=150)
    application = models.ForeignKey(Application)
    comments = models.TextField(null=True, blank=True)
    is_external = models.BooleanField(default=False)
    
    class Meta:
        unique_together = ('application', 'name')
    
    def __unicode__(self):
        return self.name

FIELD_TYPES = ['CharField',
               'ForeignKey', 'OneToOneField','ManyToManyField',
               'AutoField', 'BigIntegerField', 'BooleanField', 
               'CommaSeparatedIntegerField', 'DateField', 'DateTimeField',
               'DecimalField', 'EmailField', 'FileField', 'FilePathField',
               'FloatField', 'ImageField', 'IntegerField',  'TextField',
               'IntegerField', 'IPAddressField', 'NullBooleanField',
               'PositiveIntegerField', 'PositiveSmallIntegerField',
               'SlugField', 'SmallIntegerField', 'TextField', 'TimeField',
               'URLField', 'XMLField']

FIELD_TYPE_CHOICES = [(i,i) for i in FIELD_TYPES]

class Field(SortableModel):
    model = models.ForeignKey(Model)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=FIELD_TYPE_CHOICES) # External fileds are stored as "module.FIelName"
    relation = models.ForeignKey(Model, null=True, blank=True, related_name='related_fields')
    null = models.BooleanField()
    blank = models.BooleanField()

    class Meta:
        unique_together = ("model", "name")
        ordering = ['sort_order']

    def __unicode__(self):
        return '%s = %s()' % (self.name, self.type)
