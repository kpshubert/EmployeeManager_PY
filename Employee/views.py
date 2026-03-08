from Employee.filters import EmployeeFilter
from Employee.models import tEM_Employee
from django import forms
from django.http import HttpResponse
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, DetailView
from django_filters.views import FilterView
from django.urls import reverse_lazy
from .forms import EditEmployeeForm, CreateEmployeeForm
from utils import prepend_if_not_empty

'''
from .models import tEM_Employee
'''


# Create your views here.

def index(request):
    return HttpResponse("<h1>Hello, world. You're looking at the templates manager homepage.</h1>")

class EmployeeListView(FilterView):
    model = tEM_Employee
    paginate_by = 3
    template_name = "ListEmployees.html"
    filterset_class = EmployeeFilter
    context_object_name = "employees"

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = EmployeeFilter(self.request.GET, queryset=super().get_queryset())
        query_dict = self.request.GET.copy()
        query_dict.pop('page', True)
        context['query_string'] = prepend_if_not_empty(query_dict.urlencode(), '&')
        return context


class CreateEmployeeView(CreateView):
    model = tEM_Employee
    form_class = CreateEmployeeForm  # Use custom form with labels
    template_name = 'CreateEmployee.html'
    success_url = reverse_lazy('ListEmployees')  # Replace with your URL name
    context_object_name = "employee"

class EditEmployeeView(UpdateView):
    model = tEM_Employee
    form_class = EditEmployeeForm  # Use custom form with labels
    template_name = 'EditEmployee.html'
    success_url = reverse_lazy('ListEmployees')  # Replace with your URL name
    context_object_name = "employee"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        '''
        context['Applications'] = Application.objects.filter(vacancy_id=self.kwargs['vacancy_id'])
        '''
        return context

class DeleteEmployeeView(DeleteView):
    model = tEM_Employee
    template_name = "DeleteEmployee.html"
    context_object_name = "employee"
    success_url = reverse_lazy('ListEmployees')  # Use reverse_lazy for URLs
    failure_message = "Employee was not deleted."

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class DetailEmployeeView(DetailView):
    model = tEM_Employee
    template_name = "DetailEmploee.html"
    context_object_name = "employee"  # Optional: customize context variable name

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context