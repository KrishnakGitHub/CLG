from django import forms
from django.contrib.auth.models import User
from .models import MyUser, Student, Department, Leacturare, Employee
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm

# Sign Up Form
class StudentSignUpForm(UserCreationForm):
    department = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        required=True,
        empty_label=None)
    first_name = forms.CharField(label='First name')
    last_name = forms.CharField(label='Last name')

    class Meta(UserCreationForm.Meta):
        model = MyUser
        fields = ["username","first_name","last_name","email"]

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user, department=self.cleaned_data.get('department'))
        return user

class LecturerSignUpForm(UserCreationForm):
    department = forms.ModelMultipleChoiceField(
        queryset=Department.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta(UserCreationForm.Meta):
        model = MyUser
        fields = ["username","first_name","last_name","email"]

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_lecturer = True
        if commit:
            user.save()
            lecturer = Leacturare.objects.create(user=user)
            lecturer.department.add(*self.cleaned_data.get('department'))
        return user


class EmployeeSignUpForm(UserCreationForm):
    Employee_Type = forms.ChoiceField(
        choices=(("Pune", "Pune"), ("Sweeper", "Sweeper")),
        required=True)

    class Meta(UserCreationForm.Meta):
        model = MyUser
        fields = ["username","first_name","last_name","email"]

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_employee = True
        user.save()
        employee = Employee.objects.create(user=user, Employee_Type=self.cleaned_data.get('Employee_Type'))
        #employee.Employee_Type.add(*self.cleaned_data.get('Employee_Type'))
        return user