from django import forms
from .models import tEM_Employee

class EditEmployeeForm(forms.ModelForm):
    class Meta:
        model = tEM_Employee
        fields = ['FirstName', 'LastName', 'Phone', 'Email', 'DepartmentID']
        labels = {
            'FirstName': 'First Name',
            'LastName': 'Last Name',
            'Phone': 'Phone',
            'Email': 'Email',
            'DepartmentID': 'Department"',
        }
        widgets = {
            'DepartmentId': forms.Select(attrs={'class': 'form-control'}),
        }

class CreateEmployeeForm(forms.ModelForm):
    class Meta:
        model = tEM_Employee
        fields = ['FirstName', 'LastName', 'Phone', 'Email', 'DepartmentID']
        labels = {
            'FirstName': 'First Name',
            'LastName': 'Last Name',
            'Phone': 'Phone',
            'Email': 'Email',
            'DepartmentID': 'Department"',
        }
        widgets = {
            'DepartmentId': forms.Select(attrs={'class': 'form-control'}),
        }
