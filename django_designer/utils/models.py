from django.db import models
from django.utils.translation import ugettext_lazy as _

class SortableModel(models.Model):
    sort_order = models.IntegerField(_('sort order'))

    class Meta:
        abstract = True
        ordering = ['sort_order']

    def save(self, *args, **kwargs):
        if self.pk is None and self.sort_order is None:
            self.sort_order = self.next_sort_order()
        return super(SortableModel, self).save(*args, **kwargs)

    @classmethod
    def next_sort_order(cls):
        "Returns next sort_order value"
        try:
            return cls.objects.all().order_by('-sort_order')[0].sort_order + 1
        except IndexError:
            return 1
