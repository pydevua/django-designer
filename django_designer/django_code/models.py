FIELD_ATTRIBUTES = {
    'CharField':        ['max_length'],
    'DateField':        ['auto_now', 'auto_now_add'],
    'DateTimeField':    ['auto_now', 'auto_now_add'],
    'TimeField':        ['auto_now', 'auto_now_add'],
    'DecimalFeild':     ['max_digits', 'decimal_places'],
    'UrlField':         ['verify_exists'],
    'FileField':        ['upload_to'],
    'OneToOneField':    ['related_name', 'to_field'],
    'ForeignKey':       ['related_name', 'to_field'],
    'ManyToManyField':  ['related_name', 'to_field'],
    'OneToOneField':    ['related_name', 'to_field'],
}
