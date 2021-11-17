from django.contrib import admin
from .models import Marks, Attendance, ExamTimeTable
# Register your models here.
admin.site.register(Marks)
admin.site.register(Attendance)
admin.site.register(ExamTimeTable)
