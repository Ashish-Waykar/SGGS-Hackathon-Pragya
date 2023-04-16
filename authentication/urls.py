from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.register,name='register'),
    path('login/', views.login,name='login'),
    path('logout/', views.logout,name='logout'),
    # path('', views.dashboard,name='dashboard'),
    path('', views.dashboard,name='dashboard'),
    path('edit_profile/', views.edit_profile,name='edit_profile'),

    path('hod-student-application-details/<str:application_no>/', views.hod_student_application_details,name='hod_student_application_details'),
    path('hod-faculty-application-details/<str:application_no>/', views.hod_faculty_application_details,name='hod_faculty_application_details'),

]
