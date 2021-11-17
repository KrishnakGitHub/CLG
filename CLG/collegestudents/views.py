from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import Marks, Attendance, ExamTimeTable
from collegeapp.models import Lecture, Leacturare, Student, TimeTable, StudentFnW
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from userApp.decorators import admin_required
# Create your views here.
@method_decorator([login_required, admin_required], name='dispatch')
class CreateMarks(CreateView):
	model = Marks
	fields ="__all__"

	def get_context_data(self, **kwargs):
		kwargs['type'] = 'Create Marks'
		kwargs['subject'] = Lecture.objects.all()
		kwargs['students'] = Student.objects.all()
		kwargs['leacturare'] = Leacturare.objects.all()
		return super().get_context_data(**kwargs)

	def form_valid(self, form):
		user = form.save()
		return redirect('home')

@method_decorator([login_required, admin_required], name='dispatch')
class CreateExamTimeTable(CreateView):
	model = ExamTimeTable
	fields ="__all__"
	template_name = 'collegeapp/timetable_form.html'

	def get_context_data(self, **kwargs):
		kwargs['type'] = 'Create Exam Time Table'
		kwargs['lecture'] = Lecture.objects.all()
		return super().get_context_data(**kwargs)

	def form_valid(self, form):
		user = form.save()
		return redirect('home')

@method_decorator([login_required, admin_required], name='dispatch')
class CreateAttendance(CreateView):
	model = Attendance
	fields ="__all__"

	def get_context_data(self, **kwargs):
		kwargs['type'] = 'Create Attendance'
		kwargs['subject'] = Lecture.objects.all()
		kwargs['students'] = Student.objects.all()
		kwargs['leacturare'] = Leacturare.objects.all()
		return super().get_context_data(**kwargs)

	def form_valid(self, form):
		user = form.save()
		return redirect('home')
@login_required
def ClassRoom(request):
	type = "My ClassRoom"
	marks =''
	attendance=''
	mysubject =''
	mytimetable=['1']
	mytable=['1']
	total_attend=0
	total_mark=0
	t_attendance=0
	t_marks=0
	mystudents = ['1']
	if request.user.is_student:
		marks = Marks.objects.filter(student = request.user.student)
		c=0
		for i in marks:
			c = c+1
			total_mark = i.mark+total_mark
			t_marks = i.total_marks+t_marks
			#percentage = (total_mark/t_marks)*100
			#average = total_mark/c
		attendance = Attendance.objects.filter(student = request.user.student)
		d=0
		for j in attendance:
			d=d+1
			total_attend = j.attendance+total_attend
			t_attendance = j.total_attendance+t_attendance
			#attendance_per = (total_attend/t_attendance)*100
			#attendance_avg = total_attend/d
	if request.user.is_lecturer:
		mysubject = Lecture.objects.filter(leacturare = request.user.leacturare)
		for mysub in mysubject:
			marks = Marks.objects.filter(subject =mysub)
		for mysub in mysubject:
			mytable = TimeTable.objects.filter(lecture = mysub.id)
			mytimetable.append(mytable)
			
	context = {'type':type,'marks':marks,'attendance':attendance,'mysubject':mysubject,'marks':marks,
	'mytimetable':mytimetable,'mytable':mytable,'total_mark':total_mark,'total_attend':total_attend,'t_attendance':t_attendance}

	return render(request, 'collegestudents/ClassRoom.html',context)

@login_required
def ClassRoomList(request):
	type = "Marks & Attendance"
	marks = Marks.objects.all()
	attendance = Attendance.objects.all()

	context = {'type':type,'marks':marks,'attendance':attendance}

	return render(request, 'collegestudents/ClassRoomList.html',context)