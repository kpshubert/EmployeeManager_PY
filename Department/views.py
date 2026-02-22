# Create your views here.
from Employee.models import tEM_Department, tEM_Employee
from django.http import HttpResponse
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, DetailView
from django.core.paginator import Paginator
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .forms import EditDepartmentForm, CreateDepartmentForm
from django.db.models import Count

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
        #EmployeeCount = tem_employee.objects.annotate(Count('DepartmentId')).order_by('DepartmentId')
        context['departments'] = tEM_Department.objects.annotate(EmployeeCount = Count('tem_employee', distinct=True))

        paginator = Paginator(context['departments'], per_page=3)
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)

        context['departments'] = page

        return context

class CreateDepartmentView(CreateView):
    model = tEM_Department
    form_class =   CreateDepartmentForm  # Use custom form with labels
    template_name = 'CreateDepartment.html'
    success_url = reverse_lazy('ListDepartments')  # Replace with your URL name
    context_object_name = "department"

class EditDepartmentView(UpdateView):
    model = tEM_Department
    form_class = EditDepartmentForm  # Use custom form with labels
    template_name = 'EditDepartment.html'
    success_url = reverse_lazy('ListDepartments')  # Replace with your URL name
    context_object_name = "department"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        '''
        context['Applications'] = Application.objects.filter(vacancy_id=self.kwargs['vacancy_id'])
        '''
        return context

class DeleteDepartmentView(SuccessMessageMixin, DeleteView):
    model = tEM_Department
    template_name = "DeleteDeparment.html"
    context_object_name = "department"
    success_url = reverse_lazy('ListDepartments')  # Use reverse_lazy for URLs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['department'] = tEM_Department.objects.filter(Id=context['department'].Id).annotate(EmployeeCount = Count('tem_employee', distinct=True))

        if context['department'].exists() and context['department'].count() > 0:
            context['department'] = context['department'][0]

        return context

class DetailDepartmentView(DetailView):
    model = tEM_Department
    template_name = "DetailDepartment.html"
    context_object_name = "department"  # Optional: customize context variable name

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context