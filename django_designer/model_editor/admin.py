from django.contrib import admin
from models import Model, Field

class FieldInline(admin.TabularInline):
    model = Field
    fk_name = 'model'

class ModelAdmin(admin.ModelAdmin):
    inlines = [FieldInline]

admin.site.register(Model, ModelAdmin)
