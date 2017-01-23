import datetime

from django.test import TestCase

from dock.models import Dock, Job
from ship.models import Ship, Container


class ShipTestCase(TestCase):

    def setUp(self):
        Ship.objects.create(
            name="ship 1",
            arrival_time=datetime.datetime.now(),
            description="Historic overview"
        )

        Ship.objects.create(
            name="ship 2",
            arrival_time=datetime.datetime.now(),
            description="Historic overview"
        )

        Container.objects.create(
            name="Container 1",
            hazard='1',
            ship=Ship.objects.get(id=1)
        )

        Container.objects.create(
            name="Container 2",
            hazard='2',
            ship=Ship.objects.get(id=2)
        )

        Dock.objects.create(
            name="Dock 1"
        )

        Dock.objects.create(
            name="Dock 2"
        )

        Job.objects.create(
            dock=Dock.objects.get(id=1),
            ship=Ship.objects.get(id=1),
            job_status='2',
            start_time=datetime.datetime.now()
        )

        Job.objects.create(
            dock=Dock.objects.get(id=2),
            ship=Ship.objects.get(id=2),
            job_status='2',
            start_time=datetime.datetime.now()
        )

    def test_two_ships_in_one_dock(self):
        """
        check can status of two ships be active on the same dock
        """
        count = Job.objects.filter(
            dock=Dock.objects.get(id=2),
            job_status='2'
        ).count()
        self.assertEqual(count, 1)

        Job.objects.create(
            dock=Dock.objects.get(id=2),
            ship=Ship.objects.get(id=1),
            job_status='2',
            start_time=datetime.datetime.now()
        )

        count = Job.objects.filter(
            dock=Dock.objects.get(id=2),
            job_status='2'
        ).count()
        self.assertEqual(count, 1)
