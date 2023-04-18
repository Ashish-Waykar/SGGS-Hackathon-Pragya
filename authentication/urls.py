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
    path('list-faculties/', views.list_faculties,name='list_faculties'),
    path('list-students/', views.list_students,name='list_students'),
    path('list-hods/', views.list_hods,name='list_hods'),
    path('list-all-applications/', views.list_all_applications,name='list_all_applications'),

    path('director-application-details/<str:application_no>/', views.director_application_details,name='director_application_details'),

    path('hod-approove-application/<str:application_no>/', views.hod_approove_application,name='hod_approove_application'),
    path('hod-reject-application/<str:application_no>/', views.hod_reject_application,name='hod_reject_application'),
    path('director-approove-application/<str:application_no>/', views.director_approove_application,name='director_approove_application'),
    path('director-reject-application/<str:application_no>/', views.director_reject_application,name='director_reject_application'),

    path('hod-list-all-application-faculty', views.hod_list_all_applications_faculty,name='hod_list_all_applications_faculty'),
    path('hod-list-all-pplications-students/', views.hod_list_all_applications_students,name='hod_list_all_applications_students'),


    path('hod-list-faculties/', views.hod_list_faculties,name='hod_list_faculties'),

    path('hod-list-students/', views.hod_list_students,name='hod_list_students'),


    path('notice-01-page/', views.year_notice_01_page,name='year_notice_01_page'),
    path('year-notice-02-page/', views.year_notice_02_page,name='year_notice_02_page'),
    path('year-notice-03-page/<str:detpt>/', views.year_notice_03_page,name='year_notice_03_page'),
    path('year-notice-04-page/<str:detpt>/<str:yr>/', views.year_notice_04_page,name='year_notice_04_page'),











    # path('add-notice/', views.list_faculties,name='list_faculties'),
    # path('add-notice-hod/', views.list_students,name='list_students'),
    # path('add-notice-faculty/', views.list_hods,name='list_hods'),
    #
    # path('hod-add-notice/', views.list_faculties,name='list_faculties'),
    # path('hod-add-notice-hod/', views.list_students,name='list_students'),
    # path('hod-add-notice-faculty/', views.list_hods,name='list_hods'),

]
