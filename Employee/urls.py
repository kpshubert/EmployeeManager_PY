from django.urls import path
from django.views.generic import ListView
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("/List", views.EmployeeListView.as_view(template_name ="ListEmployees.html"), name="ListEmployees"),
    path( "/Edit/<int:pk>/", views.EditEmployeeView.as_view(template_name ="EditEmployee.html"), name="EditEmployee"),
    path("/Delete/<int:pk>/", views.DeleteEmployeeView.as_view(template_name = "DeleteEmployee.html"), name="DeleteEmployee"),
    path("/Create", views.CreateEmployeeView.as_view(template_name="CreateEmployee.html"), name="CreateEmployee"),
    path("/Detail/<int:pk>", views.DetailEmployeeView.as_view(template_name="DetailEmployee.html"), name="DetailEmployee"),
]