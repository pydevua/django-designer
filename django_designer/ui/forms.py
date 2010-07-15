from django import forms
from django.forms.models import modelformset_factory
from common.models import Application
from model_editor.models import Model, Field

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        exclude = ('project',)
    
    def __init__(self, data=None, project=None):
        self.project = project
        super(ApplicationForm, self).__init__(data)
    
    def save(self):
        obj = super(ApplicationForm, self).save(commit=False)
        obj.project = self.project
        obj.save()
        return obj
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name:
            try:
                Application.objects.get(project=self.project, name=name)#TODO: ci check ?
                raise forms.ValidationError('Application "%s" already exist' % name)
            except Application.DoesNotExist:
                pass
        return name


class NewModelForm(forms.ModelForm):
    class Meta:
        model = Model
        exclude = ('application',)
    
    def __init__(self, data, application):
        self.application = application
        super(NewModelForm, self).__init__(data)
    
    def save(self):
        obj = super(NewModelForm, self).save(commit=False)
        obj.application = self.application
        obj.save()
        return obj
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name:
            try:
                Model.objects.get(application=self.application, name=name)#TODO: ci check ?
                raise forms.ValidationError('Model "%s" already exist' % name)
            except Model.DoesNotExist:
                pass
        return name

class EditModelForm(forms.ModelForm):
    class Meta:
        model = Model
        exclude = ('application','is_external')
    
    #TODO: name validation
    

class FieldForm(forms.ModelForm):
    class Meta:
        model = Field
        exclude = ('model',)
    sort_order = forms.IntegerField(required=False
                                    , widget=forms.HiddenInput(attrs={'class':'sort_field'}))
    
    POPUP_FIELDS = ('verbose_name', 'primary_key', 'max_length', 'unique', 
                    'db_index', 'default', 'editable', 'help_text', 'auto_now', 
                    'auto_now_add', 'max_digits', 'decimal_places', 'verify_exists', 
                    'upload_to', 'related_name', 'to_field')
    
    def __init__(self, *args, **kwargs):
        super(FieldForm, self). __init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name in FieldForm.POPUP_FIELDS:
                field.label = name
    
    def visible_fields(self):
        return [field for field in self if \
                                    (not field.is_hidden) \
                                    and (not field.name in FieldForm.POPUP_FIELDS)]
    
    def popup_fields(self):
        return [field for field in self if field.name in FieldForm.POPUP_FIELDS]
    


ModelFieldFormSet = modelformset_factory(Field, extra=3, can_delete=True, form=FieldForm)
