from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from dock.models import Dock, Job
from ship.models import Ship, Container
from employee.models import Employee


def home(request):
    result = []

    for item in Dock.objects.all():
        try:
            ship = Job.objects.filter(dock=item, job_status='2').order_by('-id')[0].ship
        except IndexError:
            ship = None

        result.append(
            {
                'dock': item,
                'ship': ship
            }
        )

    context = {
        'result': result
    }
    return render(request, 'index.html', context)


def dock_detail(request, id):
    try:
        dock = Dock.objects.get(id=id)
    except Dock.DoesNotExist:
        messages.error(request, 'Dock does not exist.')
        return HttpResponseRedirect(reverse('home'))

    employee_list = Employee.objects.filter(dock=dock)

    try:
        ship = Job.objects.filter(dock=dock, job_status='2').order_by('-id')[0].ship
    except IndexError:
        ship = None

    contianer_list = []
    if ship:
        contianer_list = Container.objects.filter(ship=ship)

    context = {
        'dock': dock,
        'ship': ship,
        'contianer_list': contianer_list,
        'employee_list': employee_list,
        'total_employees': employee_list.count(),
        'total_ships_service': Job.objects.filter(dock=dock, job_status='3').count(),
        'total_enqueue_ships': Job.objects.filter(dock=dock, job_status='1').count(),
    }
    return render(request, 'detail.html', context)