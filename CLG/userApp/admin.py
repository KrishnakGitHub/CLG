from django.contrib import admin
from .models import MyUser, Department, Student, Leacturare, Employee
# # Register your models here.
admin.site.register(MyUser)
admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Leacturare)
admin.site.register(Employee)