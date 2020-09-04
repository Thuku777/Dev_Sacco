from django.contrib import admin
from .models import *

# Register your models here.
class FeatureInline(admin.StackedInline):
    model = Feature

class ServiceAdmin(admin.ModelAdmin):
    inlines = [
        FeatureInline,
    ]


admin.site.register(Service, ServiceAdmin)
