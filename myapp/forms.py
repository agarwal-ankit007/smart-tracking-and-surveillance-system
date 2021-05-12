from django import forms
from myapp.models import Employee

class Employeeform(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
