from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import Employee
from .forms import EmployeeAdminForm


class EmployeeAdmin(UserAdmin):
    form = EmployeeAdminForm

    fieldsets = UserAdmin.fieldsets + (
        (_("Employee Information"),
            {'fields': ('address', 'bank_account', 'supervisor', 'dock')}
         ),
    )


admin.site.register(Employee, EmployeeAdmin)