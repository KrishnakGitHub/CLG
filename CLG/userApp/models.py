from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
# # Create your models here.
class MyUser(AbstractUser):
	username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
	email = models.EmailField(_('email address'), unique = True)
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
	is_student = models.BooleanField(default=False)
	is_lecturer = models.BooleanField(default=False)
	is_employee = models.BooleanField(default=False)

	def __str__(self):
		return "{}".format(self.email)

class Department(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Student(models.Model):
	user = models.OneToOneField(MyUser, on_delete=models.CASCADE, related_name="student")
	department = models.ForeignKey(Department,on_delete=models.CASCADE, related_name="student_department")

	def __str__(self):
		return self.user.first_name 

class Leacturare(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    department = models.ManyToManyField(Department,related_name='leacturare')

    def __str__(self):
        return str(self.user)

class Employee(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, related_name="employee")
    Employee_Type = models.CharField(max_length=100, choices=(("Pune", "Pune"), ("Sweeper", "Sweeper")))

    def __str__(self):
        return self.user.username