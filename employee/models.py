from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from dock.models import Dock


class Employee(AbstractUser):
    address = models.CharField(
        _('Employee address'),
        max_length=90,
    )
    bank_account = models.CharField(
        _('Employee bank account number'),
        max_length=90,
    )
    supervisor = models.ForeignKey(
        "self",
        null=True,
        blank=True,
    )
    dock = models.ForeignKey(
        Dock,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _('Employee')
        verbose_name_plural = _('Employees')

    def __unicode__(self):
        if self.first_name or self.last_name:
            return '%s %s' % (self.first_name, self.last_name)
        else:
            return self.username
