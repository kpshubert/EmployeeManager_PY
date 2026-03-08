import django_filters
from .models import tEM_Employee, tEM_Department

class EmployeeFilter(django_filters.FilterSet):
    department = django_filters.ChoiceFilter(
        choices=tEM_Employee.objects.values_list('DepartmentID','DepartmentID').distinct()
    )

    class Meta:
        model = tEM_Employee
        fields = ['DepartmentID']