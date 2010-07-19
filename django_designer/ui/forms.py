from django import forms
from common.models import Application


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
