from django import forms
from Employee.models import tEM_Department

class EditDepartmentForm(forms.ModelForm):
    class Meta:
        model = tEM_Department
        fields = ['Name']
        labels = {
            'Name': 'Department Name'
        }

class CreateDepartmentForm(forms.ModelForm):
    class Meta:
        model = tEM_Department
        fields = ['Name']
        labels = {
            'Name': 'Department Name'
        }