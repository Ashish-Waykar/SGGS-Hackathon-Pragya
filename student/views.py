from django.shortcuts import render,redirect
from authentication.models import *
from applications.models import *
from .form  import *
import datetime

from django.contrib import messages
# Create your views here.
def write_application_student(request):
    if request.method=='POST':
        auth=None
        if request.user.is_authenticated:
            auth=UserProfile.objects.get(user_id=request.user.id)
        dept=department.objects.get(department_name=request.user.dept)

        appln=application()
        appln.category= request.POST.get('category')
        appln.title=request.POST.get('title')
        appln.content=request.POST.get('content')
        appln.is_published_by_student=True
        appln.department=dept
        appln.publisher_user=request.user
        appln.status="Submited"
        appln.save()

        yr=int(datetime.date.today().strftime('%Y'))
        dt = int(datetime.date.today().strftime('%d'))
        mt =int(datetime.date.today().strftime('%m'))
        d = datetime.date(yr,mt,dt)
        current_date=d.strftime('%Y%m%d')
        uk_id =current_date + str(appln.id)
        appln.application_id =uk_id
        appln.save()

        messages.success(request,'Applications Submitted Sucessfully! ')
        return redirect('dashboard')

    auth=None
    if request.user.is_authenticated:
        auth=UserProfile.objects.get(user_id=request.user.id)
    userprofile=UserProfile.objects.get(user_id=request.user.id)
    cf=CreateApplicationForm()
    context={
    "userprofile":userprofile,
    'auth':auth,
    "cf":cf,
    }
    return render(request,'student/create-application.html',context)
def student_application_details(request,application_no):
    auth=None
    if request.user.is_authenticated:
        auth=UserProfile.objects.get(user_id=request.user.id)
    userprofile=UserProfile.objects.get(user_id=request.user.id)
    appln=application.objects.get(application_id=application_no)
    context={
    "userprofile":userprofile,
    'auth':auth,
    'appln':appln,
    }
    return render(request,'student/view-application.html',context)
