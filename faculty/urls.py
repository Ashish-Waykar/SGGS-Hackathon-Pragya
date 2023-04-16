from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('write-application-faculty/', views.write_application_faculty,name='write_application_faculty'),
    path('faculty-application-details/<str:application_no>/', views.faculty_application_details,name='faculty_application_details'),
    

]
