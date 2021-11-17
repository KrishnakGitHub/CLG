"""College URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from .views import MyDeptCreate, StudentSignUpView, LecturerSignUpView, EmployeeSignUpView, UserlistView
urlpatterns = [
    path('', views.home, name=''),
    path('accounts/profile/<int:pk>/', views.profile, name='myprofile'),
    path('accounts/signup/student/', StudentSignUpView.as_view(), name='student_signup'),
    path('accounts/signup/lecturer/', LecturerSignUpView.as_view(), name='lecturer_signup'),
    path('accounts/signup/employee/', EmployeeSignUpView.as_view(), name='employee_signup'),
    path('student/list/', UserlistView.as_view(), name='users_list'),
    #path('accounts/signup/teacher/', TeacherSignUpView.as_view(), name='teacher_signup'),

    #path('crdept/', MyDeptCreate.as_view(), name="cr_dept"),
]

