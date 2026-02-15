from Employee.models import tEM_Employee
from django import forms
from django.http import HttpResponse
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, DetailView
from django.urls import reverse_lazy
from .forms import EditEmployeeForm, CreateEmployeeForm

'''
from .models import tEM_Employee
'''


# Create your views here.

def index(request):
    return HttpResponse("<h1>Hello, world. You're looking at the templates manager homepage.</h1>")

class EmployeeListView(ListView):
    model = tEM_Employee
    paginate_by = 3
    template_name = "ListEmployees.html"
    context_object_name = "employees"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class CreateEmployeeView(CreateView):
    model = tEM_Employee
    form_class = CreateEmployeeForm  # Use custom form with labels
    template_name = 'CreateEmployee.html'
    success_url = reverse_lazy('ListEmployee')  # Replace with your URL name
    context_object_name = "employee"

class EditEmployeeView(UpdateView):
    model = tEM_Employee
    form_class = EditEmployeeForm  # Use custom form with labels
    template_name = 'EditEmployee.html'
    success_url = reverse_lazy('ListEmployee')  # Replace with your URL name
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

    def get_cpntext_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
class DetailEmployeeView(DetailView):
    model = tEM_Employee
    template_name = "DetailEmploee.html"
    context_object_name = "employee"  # Optional: customize context variable name

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context