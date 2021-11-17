from django.shortcuts import render, redirect
from .models import Department, MyUser, Student, Leacturare, Employee
from collegeapp.models import StudentFnW
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .decorators import student_required, admin_required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .forms import StudentSignUpForm, LecturerSignUpForm, EmployeeSignUpForm

#from collegeapp.models import Lecture, TimeTable, Fee, Wages
# Create your views here.
@login_required
def home(request):
    myuser = MyUser.objects.all()
    lecture = Lecture.objects.all()
    timetable = TimeTable.objects.all()
    fee = Fee.objects.all()
    wages = Wages.objects.all()
    context = {'myuser':myuser,'lecture':lecture,'timetable':timetable,'fee':fee,'wages':wages}
    return render(request, 'userApp/index.html', context)

@login_required
def profile(request,pk):
    type = "Profile"
    studentfnw = ''
    if not request.user.is_superuser:
        if not request.user.is_lecturer:
            if not request.user.is_employee:
                if StudentFnW.objects.filter(student=request.user.student).exists():
                    studentfnw = StudentFnW.objects.get(student=request.user.student)
                else:
                    studentfnw = ''    
    context = {'type':type,'studentfnw':studentfnw}
    return render(request, 'userApp/profile.html', context)


@method_decorator([login_required, admin_required], name='dispatch')
class MyDeptCreate(CreateView):
    model = Department
    fields = ["name"]

@method_decorator([login_required, admin_required], name='dispatch')
class StudentSignUpView(CreateView):
    model = MyUser
    form_class = StudentSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('home')

@method_decorator([login_required, admin_required], name='dispatch')
class LecturerSignUpView(CreateView):
    model = MyUser
    form_class = LecturerSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'lecturer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('home')

@method_decorator([login_required, admin_required], name='dispatch')
class EmployeeSignUpView(CreateView):
    model = MyUser
    form_class = EmployeeSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'employee'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('home')

@method_decorator([login_required, admin_required], name='dispatch')
class UserlistView(ListView):
    model = MyUser

    def get_context_data(self, **kwargs):
        kwargs['type'] = 'Users list'
        return super().get_context_data(**kwargs)