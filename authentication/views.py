from django.shortcuts import render,redirect
from django.contrib import messages , auth
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from .models import *
from .forms import *
from hod.models import *
from student.models import *
# Create your views here.

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

        context={
        "userprofile":userprofile,
        "appln":appln,

        'auth':auth,
        }
        return render(request,"faculty/dashboard.html",context)
    if request.user.is_student:
        auth=None
        if request.user.is_authenticated:
            auth=UserProfile.objects.get(user_id=request.user.id)
        userprofile=UserProfile.objects.get(user_id=request.user.id)

        appln=application.objects.filter(publisher_user=request.user).order_by('-datetime')

        context={
        "userprofile":userprofile,
        "appln":appln,
        'auth':auth,
        }
        return render(request,"student/dashboard.html",context)
    if request.user.is_hod:
        auth=None
        if request.user.is_authenticated:
            auth=UserProfile.objects.get(user_id=request.user.id)
        userprofile=UserProfile.objects.get(user_id=request.user.id)
        appln_stu=application.objects.filter(status='Submited',is_published_by_student=True).order_by('-datetime')
        appln_fac=application.objects.filter(status='Submited',is_published_by_faculty=True).order_by('-datetime')
        context={
        "userprofile":userprofile,
        'auth':auth,
        "appln_stu":appln_stu,
        "appln_fac":appln_fac,
        }
        return render(request,"hod/dashboard.html",context)
    if request.user.is_director:
        auth=None
        if request.user.is_authenticated:
            auth=UserProfile.objects.get(user_id=request.user.id)
        userprofile=UserProfile.objects.get(user_id=request.user.id)

        context={
        "userprofile":userprofile,
        'auth':auth,
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
