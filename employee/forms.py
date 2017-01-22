from django.contrib.auth.forms import UserChangeForm
from .models import Employee


class EmployeeAdminForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Employee
