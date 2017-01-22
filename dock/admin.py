from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import Dock, Job


class DockAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)
    ordering = ('name',)


class JobAdmin(admin.ModelAdmin):
    list_display = ('id', 'dock', 'ship', 'job_status', 'start_time', 'end_time',)
    ordering = ('dock', 'ship', 'start_time', 'end_time',)


admin.site.register(Job, JobAdmin)
admin.site.register(Dock, DockAdmin)