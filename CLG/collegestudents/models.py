from django.db import models
from collegeapp.models import Lecture, Student, Leacturare
from django.db.models.deletion import CASCADE
# Create your models here.
class Marks(models.Model):
	subject = models.ForeignKey(Lecture, on_delete=CASCADE)
	mark = models.IntegerField(default=0)
	total_marks = models.IntegerField(null=True)
	student = models.ForeignKey(Student, on_delete=CASCADE)
	given_by = models.ForeignKey(Leacturare, on_delete=CASCADE)
	cr_date = models.DateTimeField(auto_now_add=True)

class Attendance(models.Model):
	subject = models.ForeignKey(Lecture, on_delete=CASCADE)
	attendance = models.IntegerField(default=0)
	total_attendance = models.IntegerField(null=True)
	student = models.ForeignKey(Student, on_delete=CASCADE)
	given_by = models.ForeignKey(Leacturare, on_delete=CASCADE)
	cr_date = models.DateTimeField(auto_now_add=True)

class ExamTimeTable(models.Model):
	place = models.CharField(max_length=100)
	#datetime = models.DateTimeField()
	date = models.DateField(default="2017-06-01")
	time = models.TimeField(default="09:00")
	cr_date = models.DateTimeField(auto_now_add=True)
	lecture = models.ForeignKey(Lecture, on_delete=CASCADE)

	def __str__(self):
		return self.lecture.subject

	class Meta:
		ordering = ['cr_date']