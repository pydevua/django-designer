from codegenerator.tools import CodeBlock, code_string


def app_models_code(application):
    code = CodeBlock(['from django.db import models'])
    code.extend(['', ''])

    for model in application.model_set.all():
        code.extend(model_code(model))
        code.extend(['', ''])
    return '\n'.join(code.lines())

def model_code(model):
    code = CodeBlock()
    model_class = code.class_(model.name, ['models.Model'])
    if model.comments:
        model_class.append('"""%s"""' % model.comments)#TODO: handle quotes in comments, make it like a method(CommentsCode(CodeBlock))
    for field in model.field_set.all():
        model_class.append(model_field_code(field))
    if model.custom_code:
        lines = [''] + model.custom_code.split('\n')
        model_class.extend(lines)
    meta = meta_code(model)
    if model.field_set.all().count() == 0 and not model.custom_code and not meta:
        model_class.append('pass')
    if meta:
        model_class.append('')
        model_class.extend(meta)
    return code

def meta_code(model):
    lines = []
    if model.unique_together.all().count():
        pairs = []
        for item in model.unique_together.all():
            fields = ["'%s'" % f.name for f in item.fields.all()]
            pairs.append('(%s)' % ', '.join(fields))
        lines.append('unique_together = (%s,)' % ', '.join(pairs))
    if len(lines) == 0:
        return None
    code = CodeBlock()
    meta = code.class_('Meta')
    meta.extend(lines)
    return code


def model_field_code(field):
    line = u'%s = models.' % field.name
    line += unicode(FieldCode(field))
    return line






class FieldCode(object):
    def __init__(self, field):
        self.field = field
    
    def __unicode__(self):
        if hasattr(self, self.field.type):
            return getattr(self, self.field.type)()
        attrs = self._common_attrs()
        return '%s(%s)' % (self.field.type, ', '.join(attrs))
    
    def _common_attrs(self):
        attributes = []
        if self.field.verbose_name:
            attributes.append('verbose_name=%s' % code_string(self.field.verbose_name))
        if self.field.primary_key:
            attributes.append('primary_key=True')
        if self.field.null:
            attributes.append('null=True')
        if self.field.blank:
            attributes.append('blank=True')
        if self.field.unique:
            attributes.append('unique=True')
        if self.field.db_index:
            attributes.append('db_index=True')
        if not self.field.editable:
            attributes.append('editable=False')
        if self.field.default:
            val = code_string(self.field.verbose_name)
            if self.field.type in ('BigIntegerField', 'BooleanField', 'FloatField', 'IntegerField', 'IntegerField','NullBooleanField','PositiveIntegerField', 'PositiveSmallIntegerField','SmallIntegerField'):
                val = self.field.default
            attributes.append('default=%s' % val)
        if self.field.help_text:
            attributes.append('help_text=%s' % code_string(self.field.help_text))
        return attributes
    
    def CharField(self):
        attrs = []
        if self.field.max_length:
            attrs.append('max_length=%s' % self.field.max_length)
        attrs.extend(self._common_attrs())
        return '%s(%s)' % (self.field.type, ', '.join(attrs))
    
    def _autonow(self):
        attrs = []
        if self.field.auto_now:
            attrs.append('auto_now=True')
        if self.field.auto_now_add:
            attrs.append('auto_now_add=True')
        attrs.extend(self._common_attrs())
        return '%s(%s)' % (self.field.type, ', '.join(attrs))
            
    DateField = _autonow
    DateTimeField = _autonow
    TimeField = _autonow
    
    def _relatedfield(self):
        attrs = []
        if self.field.relation == self.field.model:
            attrs.append("'self'")
        else:
            if self.field.relation:
                attrs.append(self.field.relation.name)
        if self.field.related_name:
            attrs.append('related_name=%s' % code_string(self.field.related_name))
        if self.field.to_field:
            attrs.append('to_field=%s' % code_string(self.field.to_field))
        attrs.extend(self._common_attrs())
        return '%s(%s)' % (self.field.type, ', '.join(attrs))
    
    OneToOneField = _relatedfield
    ForeignKey = _relatedfield
    ManyToManyField = _relatedfield
    
    def DecimalField(self):
        attrs = []
        if self.field.max_digits:
            attrs.append('max_digits=%s' % self.field.max_digits)
        if self.field.decimal_places:
            attrs.append('decimal_places=%s' % self.field.decimal_places)
        attrs.extend(self._common_attrs())
        return '%s(%s)' % (self.field.type, ', '.join(attrs))
    
    def UrlField(self):
        attrs = []
        if not self.field.verify_exists:
            attrs.append('verify_exists=False')
        attrs.extend(self._common_attrs())
        return '%s(%s)' % (self.field.type, ', '.join(attrs))
    
    def FileField(self):
        attrs = []
        if not self.field.upload_to:
            attrs.append('upload_to=%s' % code_string(self.field.upload_to))
        attrs.extend(self._common_attrs())
        return '%s(%s)' % (self.field.type, ', '.join(attrs)) 
