from django.contrib import admin
from .models import Wages, Fee, Lecture, TimeTable, StudentFnW
# Register your models here.
admin.site.register(Wages)
admin.site.register(Fee)
admin.site.register(Lecture)
admin.site.register(TimeTable)
admin.site.register(StudentFnW)