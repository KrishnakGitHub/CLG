from django.shortcuts import render, redirect
from .models import Wages, Fee, Lecture, TimeTable, StudentFnW
from collegestudents.models import Marks, Attendance, ExamTimeTable
from userApp.models import Leacturare, Student
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView

from django.contrib.auth.decorators import login_required
from userApp.decorators import student_required, admin_required, lecturer_required
from django.utils.decorators import method_decorator
# Create your views here.
@login_required
def home(request):
    type = "Dashboard"
    # marks =''
    # attendance=''
    # mysubject =''
    # mytimetable=['1']
    # mytable=['1']
    # total_attend=0
    # total_mark=0
    # t_attendance=0
    # t_marks=0
    # if request.user.myuser.is_student:
    #     marks = Marks.objects.filter(student = request.user.myuser.student)
    #     c=0
    #     for i in marks:
    #         c = c+1
    #         total_mark = i.mark+total_mark
    #         t_marks = i.total_marks+t_marks
    #         percentage = (total_mark/t_marks)*100
    #         average = total_mark/c
    #     attendance = Attendance.objects.filter(student = request.user.myuser.student)
    #     d=0
    #     for j in attendance:
    #         d=d+1
    #         total_attend = j.attendance+total_attend
    #         t_attendance = j.total_attendance+t_attendance
    #         attendance_per = (total_attend/t_attendance)*100
    #         attendance_avg = total_attend/d
    # if request.user.myuser.is_lecturer:
    #     mysubject = Lecture.objects.filter(leacturare = request.user.myuser.leacturare)
    #     for mysub in mysubject:
    #         mytable = TimeTable.objects.filter(lecture = mysub.id)
    #         mytimetable.append(mytable)

    context = {'type':type}
    return render(request, 'collegeapp/index.html', context)

@method_decorator([login_required, admin_required], name='dispatch')
class FeeCreateView(CreateView):
    model = Fee
    fields = "__all__"

    def get_context_data(self, **kwargs):
        kwargs['type'] = 'Fee Form'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('home')

@method_decorator([login_required, admin_required], name='dispatch')
class WagesCreateView(CreateView):
    model = Wages
    fields = "__all__"

    def get_context_data(self, **kwargs):
        kwargs['type'] = 'Wages Form'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('home')

@method_decorator([login_required, admin_required], name='dispatch')
class LectureCreateView(CreateView):
    model = Lecture
    fields = "__all__"

    def get_context_data(self, **kwargs):
        kwargs['type'] = 'Assign Lecture'
        kwargs['lecture'] = Lecture.objects.all()
        kwargs['Leacturare'] = Leacturare.objects.all()
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('CreateTimeTable')

@method_decorator([login_required, admin_required], name='dispatch')
class TimeTableCreateView(CreateView):
    model = TimeTable
    fields = "__all__"

    def get_context_data(self, **kwargs):
        kwargs['type'] = 'Create Time Table'
        kwargs['lecture'] = Lecture.objects.all()
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('home')

@method_decorator([login_required], name='dispatch')
class MyLectureCreateView(CreateView):
    model = Lecture
    fields = "__all__"
    template_name = "collegeapp/mylecture_form.html"

    def get_context_data(self, **kwargs):
        kwargs['type'] = 'Get Lecture'
        kwargs['Leacturare'] = Leacturare.objects.filter(user = self.request.user.myuser)
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('MyTimeTableCreate')

@method_decorator([login_required], name='dispatch')
class MyTimeTableCreateView(CreateView):
    model = TimeTable
    fields = "__all__"
    template_name = "collegeapp/mytimetable_form.html"

    def get_context_data(self, **kwargs):
        kwargs['type'] = 'Schedule Time Table'
        kwargs['lecture'] = Lecture.objects.filter(leacturare = self.request.user.myuser.leacturare)
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('home')

@method_decorator([login_required, admin_required], name='dispatch')
class FeeStatus(CreateView):
    model = StudentFnW
    fields = "__all__"

    def get_context_data(self, **kwargs):
        kwargs['type'] = 'Fee Status'
        kwargs['students'] = Student.objects.all()
        kwargs['fee'] = Fee.objects.all()
        kwargs['wages'] = Wages.objects.all()
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('home')

@method_decorator([login_required], name='dispatch')
class TimeTablelistView(ListView):
    model = TimeTable
    fields = "__all__"

    def get_context_data(self, **kwargs):
        kwargs['type'] = 'Time Table'
        kwargs['Leacturare'] = Leacturare.objects.all()
        kwargs['examtimetable'] = ExamTimeTable.objects.all()
        return super().get_context_data(**kwargs)

@method_decorator([login_required], name='dispatch')
class FeeListView(ListView):
    model = StudentFnW
    fields = "__all__"

    def get_context_data(self, **kwargs):
        kwargs['type'] = 'Fee & Wages'
        kwargs['fee'] = Fee.objects.all()
        kwargs['wages'] = Wages.objects.all()
        if StudentFnW.objects.filter(student=self.request.user.myuser.student).exists():
            kwargs['queryset'] = StudentFnW.objects.get(student=self.request.user.myuser.student)
        else:
            kwargs['queryset'] = ''    
        return super().get_context_data(**kwargs)