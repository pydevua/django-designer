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


COMMON_ATTRIBUTES = (
    'verbose_name',
    'primary_key',
    'unique', 
    'db_index',
    'default',
    'editable',
    'help_text',
)

FIELD_ATTRIBUTES = {
    'CharField':        ['max_length'],
    'DateField':        ['auto_now', 'auto_now_add'],
    'DateTimeField':    ['auto_now', 'auto_now_add'],
    'TimeField':        ['auto_now', 'auto_now_add'],
    'DecimalField':     ['max_digits', 'decimal_places'],
    'UrlField':         ['verify_exists'],
    'FileField':        ['upload_to'],
    'OneToOneField':    ['related_name', 'to_field'],
    'ForeignKey':       ['related_name', 'to_field'],
    'ManyToManyField':  ['related_name', 'to_field'],
}