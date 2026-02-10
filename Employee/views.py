from Employee.models import tEM_Employee
from django import forms
from django.http import HttpResponse
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, DetailView
from django.urls import reverse_lazy
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

class EditEmployeeView(UpdateView):
    model = tEM_Employee
    success_url = reverse_lazy('ListEmployees')  # Use reverse_lazy for URLs
    fields = ['FirstName', 'LastName', 'Phone', 'Email', 'DepartmentID']
    labels = {
        'FirstName': 'First Name',
        'LastName': 'Last Name',
        'Phone': 'Phone',
        'Email': 'Email',
        'DepartmentID': 'Department ID'
    }
    template_name = "EditEmployee.html"
    context_object_name = "employee"
    widgets = {
        'DepartmentId': forms.Select(attrs={'class': 'form-control'}),
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class DeleteEmployeeView(DeleteView):
    model = tEM_Employee
    template_name = "DeleteEmployee.html"
    context_object_name = "employee"
    success_url = reverse_lazy('ListEmployees')  # Use reverse_lazy for URLs

    def get_cpntext_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class CreateEmployeeView(CreateView):
    model = tEM_Employee
    fields = ['FirstName', 'LastName', 'Phone', 'Email', 'DepartmentID']
    success_url = reverse_lazy('ListEmployees')  # Use reverse_lazy for URLs

class DetailEmployeeView(DetailView):
    model = tEM_Employee
    template_name = "DetailEmploee.html"
    context_object_name = "employee"  # Optional: customize context variable name

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context