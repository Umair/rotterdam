from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

HAZARD_CHOICES = (
    ('0', _("No hazard")),
    ('1', _("Fire hazard")),
    ('2', _("Chemical hazard")),
)


class Ship(models.Model):
    name = models.CharField(
        _('Ship unique identifier'),
        max_length=150,
        unique=True,
    )
    arrival_time = models.DateTimeField(
        _('Ship arrival time'),
    )
    description = models.TextField(
        _("Historic overview"),
    )

    class Meta:
        verbose_name = _('Ship')
        verbose_name_plural = _('Ships')

    def __unicode__(self):
        return self.name

    def get_hazard_status(self):
        if Container.objects.filter(ship=self, hazard__in=['1', '2']).exists():
            return "Hazardies"
        return "No hazard"


class Container(models.Model):
    name = models.CharField(
        _('Container unique identifier'),
        max_length=150,
        unique=True,
    )
    ship = models.ForeignKey(
        Ship,
    )
    hazard = models.CharField(
        max_length=1,
        choices=HAZARD_CHOICES
    )

    class Meta:
        verbose_name = _('Container')
        verbose_name_plural = _('Containers')

    def __unicode__(self):
        return self.name
