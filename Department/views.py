from django.shortcuts import render

# Create your views here.
from django import forms
from Employee.models import tEM_Department
from django import forms
from django.http import HttpResponse
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, DetailView
from django.urls import reverse_lazy

# Create your views here.

def index(request):
    return HttpResponse("<h1>You're looking at the templates home page in the EmployeeManager.</h1>")

class DepartmentListView(ListView):
    model = tEM_Department
    paginate_by = 3
    template_name = "ListDepartments.html"
    context_object_name = "departments"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class EditDepartmentView(UpdateView):
    model = tEM_Department
    success_url = reverse_lazy('ListDepartments')  # Use reverse_lazy for URLs
    fields = ['Name' ]
    labels = {
        'Name': 'Department Name',
    }
    template_name = "EditEmployee.html"
    context_object_name = "department"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class DeleteDepartmentView(DeleteView):
    model = tEM_Department
    template_name = "DeleteDeparment.html"
    context_object_name = "department"
    success_url = reverse_lazy('ListDepartments')  # Use reverse_lazy for URLs

    def get_cpntext_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class CreateDepartmentView(CreateView):
    model = tEM_Department
    fields = ['Name']
    success_url = reverse_lazy('ListDepartments')  # Use reverse_lazy for URLs

class DetailDepartmentView(DetailView):
    model = tEM_Department
    template_name = "DetailDepartment.html"
    context_object_name = "department"  # Optional: customize context variable name

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context