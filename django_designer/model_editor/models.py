from django.db import models
from django_code.models import FIELD_TYPES
from common.models import Application
from utils.models import SortableModel

class Model(models.Model):
    "Django model"
    name = models.CharField(max_length=150)
    application = models.ForeignKey(Application)
    comments = models.TextField(null=True, blank=True)
    custom_code = models.TextField(null=True, blank=True, help_text="Custom lines of class code")
    is_external = models.BooleanField(default=False)
    
    class Meta:
        unique_together = ('application', 'name')
    
    def __unicode__(self):
        return u'%s.%s' %(self.application.name, self.name)


FIELD_TYPE_CHOICES = [(i,i) for i in FIELD_TYPES]

class Field(SortableModel):
    model = models.ForeignKey(Model)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=FIELD_TYPE_CHOICES) # External fileds are stored as "module.FIelName"
    relation = models.ForeignKey(Model, null=True, blank=True, related_name='related_fields')
    null = models.BooleanField()
    blank = models.BooleanField()
    
    verbose_name = models.CharField(max_length=250, null=True, blank=True)
    primary_key = models.BooleanField()
    max_length = models.IntegerField(null=True, blank=True)
    unique = models.BooleanField() 
    db_index = models.BooleanField()
    default = models.CharField(max_length=250, null=True, blank=True)
    editable = models.BooleanField()
    help_text = models.CharField(max_length=250, null=True, blank=True)
    
    #Date/Time fields
    auto_now = models.BooleanField()
    auto_now_add = models.BooleanField()
    
    #Decimal field
    max_digits = models.IntegerField(null=True, blank=True)
    decimal_places = models.IntegerField(null=True, blank=True)
    
    #UrlField
    verify_exists = models.BooleanField(default=True)
    
    #File field
    upload_to = models.CharField(max_length=250, null=True, blank=True)
    
    #Related fields
    related_name = models.CharField(max_length=250, null=True, blank=True)
    to_field = models.CharField(max_length=250, null=True, blank=True)
    #through = FK(Model)

    class Meta:
        unique_together = ("model", "name")
        ordering = ['sort_order']

    def __unicode__(self):
        return '%s = %s()' % (self.name, self.type)
