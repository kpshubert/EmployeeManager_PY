from django.urls import path
from django.views.generic import ListView
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("List", views.DepartmentListView.as_view(template_name ="ListDepartments.html"), name="ListDepartments"),
    path( "Edit/<int:pk>/", views.EditDepartmentView.as_view(template_name ="EditDepartment.html"), name="EditDepartment"),
    path("Delete/<int:pk>/", views.DeleteDepartmentView.as_view(template_name = "DeleteDepartment.html"), name="DeleteDepartment"),
    path("Create", views.CreateDepartmentView.as_view(template_name="CreateDepartment.html"), name="CreateDepartment"),
    path("Detail/<int:pk>", views.DetailDepartmentView.as_view(template_name="DetailDepartment.html"), name="DetailDepartment"),
]