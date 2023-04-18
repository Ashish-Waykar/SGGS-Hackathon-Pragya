from django.shortcuts import render,redirect
from django.contrib import messages , auth
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage

from hod.models import *
from student.models import *
from notices.models import *




def index(request):
    context={
    "clg":"Shree Guru Gobind Singhji College Of Engineeiring ."
    }
    return render(request,"home.html",context)
