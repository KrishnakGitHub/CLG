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
from .views import (FeeCreateView, WagesCreateView, LectureCreateView, TimeTableCreateView, MyLectureCreateView, MyTimeTableCreateView, TimeTablelistView,
FeeStatus, FeeListView)
urlpatterns = [
    path('', views.home, name="home"),
    path('CreateFee/', FeeCreateView.as_view(), name='CreateFee'),
    path('FeeStatuscreate/', FeeStatus.as_view(), name='Feestatuscreate'),
    path('CreateWages/', WagesCreateView.as_view(), name='CreateWages'),
    path('CreateLecture/', LectureCreateView.as_view(), name='CreateLecture'),
    path('CreateTimeTable/', TimeTableCreateView.as_view(), name='CreateTimeTable'),
    path('MyLectureCreate/', MyLectureCreateView.as_view(), name='MyLectureCreate'),
    path('MyTimeTableCreate/', MyTimeTableCreateView.as_view(), name='MyTimeTableCreate'),
    path('timeTablelistView/', TimeTablelistView.as_view(), name='TimeTablelistView'),

    path('FeeStatus/', FeeListView.as_view(), name='Feestatus'),
]
