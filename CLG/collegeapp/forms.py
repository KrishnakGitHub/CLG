from django import forms
from django.contrib.auth.models import User
from .models import Wages, Fee, Lecture, TimeTable, StudentFnW
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm

# Sign Up Form
class CreateFeeForm(forms.ModelForm):
    class Meta:
        model = Fee
        fields = "__all__"

class CreateWagesForm(forms.ModelForm):
    class Meta:
        model = Wages
        fields = "__all__"

class CreateLectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = "__all__"

class CreateTimeTableForm(forms.ModelForm):
    class Meta:
        model = TimeTable
        fields = "__all__"

class StudentFnwForm(forms.ModelForm):
    
    class Meta:
        model = StudentFnW
        fields = "__all__"