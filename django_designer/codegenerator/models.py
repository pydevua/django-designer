from codegenerator.tools import CodeBlock


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
    if model.field_set.all().count() == 0:
        model_class.append('pass')
    return code


def model_field_code(field):
    line = '%s = models.%s' % (field.name, field.type)
    attributes = []
    if field.type == 'CharField':
        attributes.append('max_length=255')
    elif field.type == 'ForeignKey' or field.type == 'ManyToManyField' \
                                    or field.type == 'OneToOneField':
        if field.relation == field.model:
            attributes.append("'self'")
        else:
            attributes.append(field.relation.name)
    if field.null:
        attributes.append('null=True')
    if field.blank:
        attributes.append('blank=True')
    line += '(' + ', '.join(attributes) +')'
    return line
