from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _

from ship.models import Ship


JOB_STATUS = (
    ('1', _("Enqueue")),
    ('2', _("Active Job")),
    ('3', _("Job done | Dequeue")),
)


class Dock(models.Model):
    name = models.CharField(
        _('Dock unique identifier'),
        max_length=150,
        unique=True,
    )

    class Meta:
        verbose_name = _('Dock')
        verbose_name_plural = _('Docks')

    def __unicode__(self):
        return self.name

    def get_active_job(self):
        try:
            return Job.objects.get(dock=self, job_status=2)
        except Job.DoesNotExist:
            return None


class Job(models.Model):
    dock = models.ForeignKey(
        Dock
    )
    ship = models.ForeignKey(
        Ship
    )
    job_status = models.CharField(
        choices=JOB_STATUS,
        max_length=1
    )
    start_time = models.DateTimeField(
        _("Job start date and time")
    )
    end_time = models.DateTimeField(
        _("Job end date and time"),
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _('Jobs')
        verbose_name_plural = _('Jobs')
        unique_together = (("dock", "ship"),)

    def __unicode__(self):
        return '%s %s'% (self.dock.name, self.ship.name)

    def save(self, *args, **kwargs):
        if not self.id and not Job.objects.\
                filter(dock=self.dock, job_status='2').exists():
            super(Job, self).save(*args, **kwargs)
        return