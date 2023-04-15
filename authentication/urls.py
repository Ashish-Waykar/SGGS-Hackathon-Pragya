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
]
