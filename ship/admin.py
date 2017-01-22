from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import Ship, Container


class ShipAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'arrival_time',)
    search_fields = ('name',)
    ordering = ('name',)


class ContainerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'ship', 'hazard',)
    search_fields = ('name', 'ship',)
    ordering = ('name', 'ship',)


admin.site.register(Container, ContainerAdmin)
admin.site.register(Ship, ShipAdmin)