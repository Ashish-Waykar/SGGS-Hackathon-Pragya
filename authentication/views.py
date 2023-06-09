from django.shortcuts import render,redirect
from django.contrib import messages , auth
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from .models import *
from .forms import *
from hod.models import *
from student.models import *
from notices.models import *
# Create your views here.
def year_notice_01_page(request):
    auth=None
    if request.user.is_authenticated:
        auth=UserProfile.objects.get(user_id=request.user.id)
    userprofile=UserProfile.objects.get(user_id=request.user.id)

    context={
    "userprofile":userprofile,
    'auth':auth,
    }
    return render(request,"director/notice/notice-page1.html",context)
def year_notice_02_page(request):
    auth=None
    if request.user.is_authenticated:
        auth=UserProfile.objects.get(user_id=request.user.id)
    userprofile=UserProfile.objects.get(user_id=request.user.id)
    departments= department.objects.all()

    context={
    "departments":departments,
    "userprofile":userprofile,
    'auth':auth,
    }
    return render(request,"director/notice/notice-page2.html",context)
def year_notice_03_page(request,detpt):
    auth=None
    if request.user.is_authenticated:
        auth=UserProfile.objects.get(user_id=request.user.id)
    userprofile=UserProfile.objects.get(user_id=request.user.id)
    departments= detpt

    yr_1="1st Year"
    yr_2="2nd Year"
    yr_3="3rd Year"
    yr_4="4th Year"
    context={
    "userprofile":userprofile,
    'auth':auth,
    "d":departments,
    "yr_1":yr_1,
    "yr_2":yr_2,
    "yr_3":yr_3,
    "yr_4":yr_4,
    }
    return render(request,"director/notice/notice-page3.html",context)
def year_notice_04_page(request,detpt,yr):
    auth=None
    if request.user.is_authenticated:
        auth=UserProfile.objects.get(user_id=request.user.id)
    userprofile=UserProfile.objects.get(user_id=request.user.id)
    if request.method == 'POST':
        tit = request.POST.get('title')
        cont = request.POST.get('content')
        # content = request.POST.get('content')
        dept=department.objects.get(department_name=detpt)

        notice=Notice()
        notice.from_head_user_by="Director"
        notice.for_director_to="For Year(Director)"
        notice.publish_to_yr=yr
        notice.title=tit
        notice.content=cont
        notice.department=dept
        notice.is_by_director=True
        notice.is_for_all_students=True
        notice.save()
        messages.success(request,'Notice Has Been Successfully Posted for Year',yr)
        return redirect('dashboard')
    dept=detpt
    yrr=yr
    context={
    "detpt":dept,
    "yr":yrr,
    "userprofile":userprofile,
    'auth':auth,
    }
    return render(request,"director/notice/notice-page5.html",context)

def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    company=False
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        # print(form)
        print(form.errors)
        if form.is_valid():

            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            dob = form.cleaned_data['dob']
            yr = form.cleaned_data['year']
            deptrt = form.cleaned_data['dept']
            password = form.cleaned_data['password']
            username = email.split("@")[0]
            user = Account.objects.create_user(dept=deptrt,year =yr ,first_name=first_name,last_name=last_name,phone_number=phone_number,email=email,username=username,password=password,dob=dob)
            user.save()
# Createthe user profile_form
            profile = UserProfile()
            profile.user_id=user.id
            profile.city="Nanded"
            profile.state="Maharashtra"
            profile.reg_no= email.split("@")[0]
            profile.save()
            # student
            dept=department.objects.get(department_name=deptrt)
            stu=student()
            stu.year=yr
            stu.department=dept
            stu.user=user
            stu.save()
            # User Activation
            # current_site= get_current_site(request)
            # mail_subject = "New Account Activation Verify Your Email "
            # message = render_to_string('mails/registration_verification_email.html',{
            #     'user': user,
            #     'domain':current_site,
            #     'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            #     'token':default_token_generator.make_token(user),
            #
            # })
            # to_email=email
            # send_email=EmailMessage(mail_subject,message,to=[to_email])
            # send_email.content_subtype='html'
            # send_email.send()

            messages.success(request,'Thank You for registaring with us ,Please Go Through Your Email to activate your account  ...')
            return redirect('/authentication/login/?command=verification&email='+email)
    else:
        form = RegistrationForm()
    context = {
    'form':form,
    # 'newsletter_form': newsletter_form,
    }
    return render(request,'authentication/login-register.html',context)

def login(request):
    if request.user.is_authenticated:
            return redirect('dashboard')
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,' You Are Now Logged In...')
            return redirect('dashboard')
            url=request.META.get('HTTP_REFERER')
            try:
                query=requests.utils.urlparse(url).query
                params=dict(x.split('=') for x in query.split('&'))
                if 'next' in params:
                    nextPage=params['next']
                    return redirect(nextPage)
            except:
                return redirect('dashboard')
        else:
            messages.error(request,' Invalid Login Credentials ! ')
            return redirect('login')
    # print("in The Login")
    form = RegistrationForm()
    context = {
    'form':form,
    # 'newsletter_form': newsletter_form,
    }
    return render(request,'authentication/login-register.html',context)

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request,' You Are Now Logged Out...')
    return redirect('login')

@login_required(login_url='login')
def dashboard(request):
    if request.user.is_faculty:
        auth=None
        if request.user.is_authenticated:
            auth=UserProfile.objects.get(user_id=request.user.id)
        userprofile=UserProfile.objects.get(user_id=request.user.id)
        appln=application.objects.filter(publisher_user=request.user).order_by('-datetime')
        appln_approoved=application.objects.filter(publisher_user=request.user,status="Approoved").count()
        appln_hod=application.objects.filter(publisher_user=request.user,status="Accepted Level 1").count()
        appln_Submited=application.objects.filter(publisher_user=request.user,status="Submited").count()
        appln_Rejected=application.objects.filter(publisher_user=request.user,status="Rejected").count()
        appln_count=application.objects.filter(publisher_user=request.user).count()


        context={
        "userprofile":userprofile,
        "appln":appln,
        'auth':auth,
        "appln_approoved":appln_approoved,
        "appln_hod":appln_hod,
        "appln_Submited":appln_Submited,
        "appln_Rejected":appln_Rejected,
        "appln_count":appln_count
        }
        return render(request,"faculty/dashboard.html",context)
    if request.user.is_student:
        auth=None
        notices_yr=None
        if request.user.is_authenticated:
            auth=UserProfile.objects.get(user_id=request.user.id)
        userprofile=UserProfile.objects.get(user_id=request.user.id)

        appln=application.objects.filter(publisher_user=request.user).order_by('-datetime')
        appln_approoved=application.objects.filter(publisher_user=request.user,status="Approoved").count()
        appln_hod=application.objects.filter(publisher_user=request.user,status="Accepted Level 1").count()
        appln_Submited=application.objects.filter(publisher_user=request.user,status="Submited").count()
        appln_Rejected=application.objects.filter(publisher_user=request.user,status="Rejected").count()
        appln_count=application.objects.filter(publisher_user=request.user).count()

        if auth.user.yer :
            notices_yr= Notice.objects.filter(publish_to_yr=auth.user.yer,is_for_all_students=True).order_by("-datetime")

        context={
        "userprofile":userprofile,
        "appln":appln,
        "notices_yr":notices_yr,
        'auth':auth,
        "appln_approoved":appln_approoved,
        "appln_hod":appln_hod,
        "appln_Submited":appln_Submited,
        "appln_Rejected":appln_Rejected,
        "appln_count":appln_count
        }
        return render(request,"student/dashboard.html",context)
    if request.user.is_hod:
        auth=None
        if request.user.is_authenticated:
            auth=UserProfile.objects.get(user_id=request.user.id)
        userprofile=UserProfile.objects.get(user_id=request.user.id)
        dept=department.objects.get(department_name=auth.user.dept)
        appln_stu=application.objects.filter(status='Submited',department=dept,is_published_by_student=True).order_by('-datetime')
        appln_fac=application.objects.filter(status='Submited',department=dept,is_published_by_faculty=True).order_by('-datetime')
        accs_fac=Account.objects.filter(is_faculty=True,dept=request.user.dept,is_active=True).count()
        accs_stu=Account.objects.filter(is_student=True,dept=request.user.dept,is_active=True).count()
        appln_counts=application.objects.all().count()
        context={
        "userprofile":userprofile,
        'auth':auth,
        "appln_counts":appln_counts,
        "appln_stu":appln_stu,
        "appln_fac":appln_fac,
        "accs_stu":accs_stu,
        "accs_fac":accs_fac,
        }
        return render(request,"hod/dashboard.html",context)
    if request.user.is_director:
        auth=None
        if request.user.is_authenticated:
            auth=UserProfile.objects.get(user_id=request.user.id)
        userprofile=UserProfile.objects.get(user_id=request.user.id)
        accs_fac=Account.objects.filter(is_faculty=True,is_active=True).count()
        accs_stu=Account.objects.filter(is_student=True,is_active=True).count()
        accs_hod=Account.objects.filter(is_hod=True,is_active=True).count()

        appln_stu=application.objects.filter(status='Accepted Level 1',is_published_by_student=True).order_by('-datetime')
        appln_fac=application.objects.filter(status='Accepted Level 1',is_published_by_faculty=True).order_by('-datetime')
        context={
        "userprofile":userprofile,
        'auth':auth,
        'accs_fac':accs_fac,
        'accs_stu':accs_stu,
        'accs_hod':accs_hod,
        'appln_stu':appln_stu,
        'appln_fac':appln_fac,
        }
        return render(request,"director/dashboard.html",context)





@login_required(login_url='login')
def edit_profile(request):
    userprofile =get_object_or_404(UserProfile,user=request.user)
    auth=None
    if request.user.is_authenticated:
        auth=UserProfile.objects.get(user_id=request.user.id)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST,request.FILES, instance=userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,"Your Profile has Been Updated ! ")
            return redirect('edit_profile')
    else :
        user_form=UserForm(instance = request.user)
        profile_form=UserProfileForm(instance=userprofile)
        # from catagory.models import Links
        # try:
        #     link=Links.objects.get(title="Tutorial",is_active=True)
        # except Exception as e:
        #     link=None
        context={
        'user_form':user_form,
        # 'profile_form':profile_form,
        # 'link':link,
    # 'newsletter_form': newsletter_form,
    'auth':auth,

        'userprofile':userprofile,
        }
    return render(request, 'profile/edit_profile.html',context)



def hod_student_application_details(request,application_no):
    auth=None
    if request.user.is_authenticated:
        auth=UserProfile.objects.get(user_id=request.user.id)
    userprofile=UserProfile.objects.get(user_id=request.user.id)
    appln=application.objects.get(application_id=application_no)
    print(appln)
    context={
    "userprofile":userprofile,
    'auth':auth,
    'appln':appln,
    }
    return render(request,"hod/view-application-student.html",context)
def hod_faculty_application_details(request,application_no):
    auth=None
    if request.user.is_authenticated:
        auth=UserProfile.objects.get(user_id=request.user.id)
    userprofile=UserProfile.objects.get(user_id=request.user.id)
    appln=application.objects.get(application_id=application_no)
    print(appln)
    context={
    "userprofile":userprofile,
    'auth':auth,
    'appln':appln,
    }
    return render(request,"hod/view-application-faculty.html",context)



def list_faculties(request):
    auth=None
    if request.user.is_authenticated:
        auth=UserProfile.objects.get(user_id=request.user.id)
    userprofile=UserProfile.objects.get(user_id=request.user.id)
    accs=Account.objects.filter(is_faculty=True,is_active=True)

    context={
    "userprofile":userprofile,
    'auth':auth,
    'accs':accs,
    }
    return render(request,"director/list-faculties.html",context)

def list_students(request):
    auth=None
    if request.user.is_authenticated:
        auth=UserProfile.objects.get(user_id=request.user.id)
    userprofile=UserProfile.objects.get(user_id=request.user.id)
    acc_verified=Account.objects.filter(is_student=True,is_active=True)
    acc_nonverified=Account.objects.filter(is_student=True,is_active=False)

    context={
    "userprofile":userprofile,
    'auth':auth,
    'acc_verified':acc_verified,
'acc_nonverified':acc_nonverified,
    }
    return render(request,"director/list-students.html",context)

def list_hods(request):
    auth=None
    if request.user.is_authenticated:
        auth=UserProfile.objects.get(user_id=request.user.id)
    userprofile=UserProfile.objects.get(user_id=request.user.id)
    accs=Account.objects.filter(is_hod=True,is_active=True)

    context={
    "userprofile":userprofile,
    'auth':auth,
    'accs':accs,
    }
    return render(request,"director/list-hods.html",context)
def list_all_applications(request):
    auth=None
    if request.user.is_authenticated:
        auth=UserProfile.objects.get(user_id=request.user.id)
    userprofile=UserProfile.objects.get(user_id=request.user.id)
    applications_sub=application.objects.filter(status="Submited")
    applications_acc=application.objects.filter(status="Accepted Level 1")
    applications_app=application.objects.filter(status="Approoved")
    applications_rej=application.objects.filter(status="Rejected")




    context={
    "userprofile":userprofile,
    'auth':auth,
    # 'accs':accs,
    "applications_sub":applications_sub,
    "applications_acc":applications_acc,
    "applications_app":applications_app,
    "applications_rej":applications_rej,
    }
    return render(request,'director/applications/list-all-aplications.html',context)


def director_application_details(request,application_no):

    auth=None
    if request.user.is_authenticated:
        auth=UserProfile.objects.get(user_id=request.user.id)
    userprofile=UserProfile.objects.get(user_id=request.user.id)
    appln=application.objects.get(application_id=application_no)
    print(appln)
    context={
    "userprofile":userprofile,
    'auth':auth,
    'appln':appln,
    }
    return render(request,'director/view-application.html',context)


def hod_approove_application(request,application_no):
    auth=None
    if request.user.is_authenticated:
        auth=UserProfile.objects.get(user_id=request.user.id)
        userprofile=UserProfile.objects.get(user_id=request.user.id)
        appln=application.objects.get(application_id=application_no)
        appln.status="Accepted Level 1"
        appln.save()
        messages.success(request,'Aplication Has Been Approoved At Departmental Level...')
        # 'Approoved'
        print(appln)
    return redirect('dashboard')

def hod_reject_application(request,application_no):
    auth=None
    if request.user.is_authenticated:
        auth=UserProfile.objects.get(user_id=request.user.id)
        userprofile=UserProfile.objects.get(user_id=request.user.id)
        if request.method == 'POST':
            appln=application.objects.get(application_id=application_no)
            appln.status="Rejected"
            appln.reject_reason=request.POST.get("reject_reason")
            appln.is_rejected_by_hod=True
            appln.save()
            messages.success(request,'Aplication Has Been Rejected At Departmental Level...')
            # 'Approoved'
            return redirect('dashboard')
        else:
            appln=application.objects.get(application_id=application_no)
            context={
            "userprofile":userprofile,
            'auth':auth,
            'appln':appln,
            }
            return render(request,'hod/reject-application.html',context)



def director_approove_application(request,application_no):
    auth=None
    if request.user.is_authenticated:
        auth=UserProfile.objects.get(user_id=request.user.id)

        appln=application.objects.get(application_id=application_no)
        appln.status="Approoved"
        appln.save()
        messages.success(request,'Aplication Has Been Approoved At College Level...')
            # 'Approoved'
        return redirect('dashboard')

def director_reject_application(request,application_no):
    auth=None
    if request.user.is_authenticated:
        auth=UserProfile.objects.get(user_id=request.user.id)
        userprofile=UserProfile.objects.get(user_id=request.user.id)
        if request.method == 'POST':
            appln=application.objects.get(application_id=application_no)
            appln.status="Rejected"
            appln.reject_reason=request.POST.get("reject_reason")
            appln.is_rejected_by_director=True
            appln.save()
            messages.success(request,'Aplication Has Been Rejected At College Level...')
            # 'Approoved'
            return redirect('dashboard')

        else:
            appln=application.objects.get(application_id=application_no)
            context={
            "userprofile":userprofile,
            'auth':auth,
            'appln':appln,
            }
            return render(request,'director/reject-application.html',context)


def hod_list_all_applications_faculty(request):
    auth=None
    if request.user.is_authenticated:
        auth=UserProfile.objects.get(user_id=request.user.id)
    userprofile=UserProfile.objects.get(user_id=request.user.id)
    # accs=Account.objects.filter(is_hod=True,is_active=True)
    dept=department.objects.get(department_name=auth.user.dept)
    appln_acc=application.objects.filter(department=dept,is_published_by_faculty=True).exclude(status="Rejected").order_by('-datetime')
    appln_rej=application.objects.filter(department=dept,is_published_by_faculty=True,status="Rejected").order_by('-datetime')
    print(appln_acc)
    print(appln_rej)
    context={
    "userprofile":userprofile,
    'auth':auth,
    # 'accs':accs,
    "appln_rej":appln_acc,
    "appln_acc":appln_rej,

    }
    return render(request,'hod/view-all-applications-faculty.html',context)
def hod_list_all_applications_students(request):
    auth=None
    if request.user.is_authenticated:
        auth=UserProfile.objects.get(user_id=request.user.id)
    userprofile=UserProfile.objects.get(user_id=request.user.id)
    # accs=Account.objects.filter(is_hod=True,is_active=True)
    # print(auth.user.dept)
    dept=department.objects.get(department_name=auth.user.dept)
    appln_acc=application.objects.filter(department=dept,is_published_by_student=True).exclude(status="Rejected").order_by('-datetime')
    appln_rej=application.objects.filter(department=dept,is_published_by_student=True,status="Rejected").order_by('-datetime')
    print(appln_acc)
    print(appln_rej)
    context={
    "userprofile":userprofile,
    'auth':auth,
    # 'accs':accs,

        "appln_rej":appln_acc,
        "appln_acc":appln_rej,
    }
    return render(request,'hod/view-all-applications-students.html',context)




def hod_list_faculties(request):
    auth=None
    if request.user.is_authenticated:
        auth=UserProfile.objects.get(user_id=request.user.id)
    userprofile=UserProfile.objects.get(user_id=request.user.id)
    acc_verified=Account.objects.filter(is_faculty=True,dept=request.user.dept,is_active=True)
    acc_nonverified=Account.objects.filter(is_faculty=True,dept=request.user.dept,is_active=False)

    context={
    "userprofile":userprofile,
    'auth':auth,

    'acc_verified':acc_verified,
    'acc_nonverified':acc_nonverified,
    }
    return render(request,"hod/list-faculties.html",context)

def hod_list_students(request):
    auth=None
    if request.user.is_authenticated:
        auth=UserProfile.objects.get(user_id=request.user.id)
    userprofile=UserProfile.objects.get(user_id=request.user.id)
    acc_verified=Account.objects.filter(is_student=True,dept=request.user.dept,is_active=True)
    acc_nonverified=Account.objects.filter(is_student=True,dept=request.user.dept,is_active=False)
    context={
    "userprofile":userprofile,
    'auth':auth,
    'acc_verified':acc_verified,
    'acc_nonverified':acc_nonverified,
    }
    return render(request,"hod/list-students.html",context)
