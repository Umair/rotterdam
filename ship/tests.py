import datetime

from django.test import TestCase, Client
from django.urls import reverse

from dock.models import Dock, Job
from ship.models import Ship, Container
from employee.models import Employee


class ShipTestCase(TestCase):

    def setUp(self):
        # Test definitions as before.
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

    def test_home_page_status(self):
        """
        call home page and check its status
        """
        client = Client()
        response = client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_dock_detail_page_status(self):
        """
        call dock detail page and check its status
        """
        client = Client()
        response = client.get(reverse('dock_detail', kwargs={'id': 1}))
        self.assertEqual(response.status_code, 200)

    def test_dock_detail_page_response(self):
        """
        call dock detail page, check its status
        and check the returned dock object
        """
        client = Client()
        response = client.get(reverse('dock_detail', kwargs={'id': 1}))
        dock = Dock.objects.get(id=1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['dock'].id, dock.id)
