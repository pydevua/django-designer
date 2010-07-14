from django.contrib.admin.util import NestedObjects
from django.utils.encoding import force_unicode
from django.utils.text import capfirst
from django.utils.safestring import mark_safe
from django.utils.html import escape


def _format_callback(obj):
    opts = obj._meta
    if hasattr(obj, 'get_absolute_url'):
        return mark_safe(u'%s: <a href="%s">%s</a>' %
                         (escape(capfirst(opts.verbose_name)),
                          obj.get_absolute_url(),
                          escape(obj)))
    else:
        return u'%s: %s' % (capfirst(opts.verbose_name),
                           force_unicode(obj))

def get_deleted_objects(obj):
    """
    Find all objects related to ``objs`` that should also be
    deleted. ``objs`` should be an iterable of objects.

    Returns a nested list of strings suitable for display in the
    template with the ``unordered_list`` filter.
    """

    collector = NestedObjects()

    obj._collect_sub_objects(collector)

    to_delete = collector.nested(_format_callback)

    return to_delete
