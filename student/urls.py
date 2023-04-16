from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('write-application-student/', views.write_application_student,name='write_application_student'),
    path('student-application-details/<str:application_no>/', views.student_application_details,name='student_application_details')
]
