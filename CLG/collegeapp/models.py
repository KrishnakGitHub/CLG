from django.db import models
from userApp.models import Department,Student, Leacturare
from django.db.models.deletion import CASCADE
# Create your models here.

class Wages(models.Model):
	name = models.CharField(max_length=100)
	amount = models.IntegerField(default=0, null=True)
	def __str__(self):
		return self.name

class Fee(models.Model):
	name = models.CharField(max_length=100)
	course_fee = models.IntegerField(default=0, null=True)
	
	def __str__(self):
		return self.name

class StudentFnW(models.Model):
	student = models.ForeignKey(Student, on_delete=CASCADE)
	fee = models.ForeignKey(Fee, on_delete=CASCADE)
	wages = models.ForeignKey(Wages, on_delete=CASCADE)
	is_fee_pending = models.BooleanField(default=False)
	is_wages_pending = models.BooleanField(default=False)

class Lecture(models.Model):
	subject = models.CharField(max_length=100)
	cr_date = models.DateTimeField(auto_now_add=True)
	leacturare = models.ForeignKey(Leacturare,on_delete=CASCADE, default="1")

	def __str__(self):
		return str(self.subject)

	class Meta:
		ordering = ['cr_date']

class TimeTable(models.Model):
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