from django.db import models

from django.contrib.auth.models import AbstractBaseUser , BaseUserManager
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image , ImageDraw
# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self,first_name,last_name,username,phone_number,email,dob,password=None):
        if not email:
            raise ValueError('User Must Have An Email Address')

        if not username:
            raise ValueError('User Must Have An Username ')

        user=self.model(
            email=self.normalize_email(email),# these normailze will normalize our email from capital to small letters for eg AASHISHwaykar19@gmail.com=ashish19@gmail.com
            username=username,
            first_name=first_name,
            phone_number=phone_number,
            last_name=last_name,
            dob=dob,

        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,first_name,last_name,email,username,password,phone_number):
        user = self.create_user(
            email=self.normalize_email(email),# these normailze will normalize our email from capital to small letters for eg AASHISHwaykar19@gmail.com=ashish19@gmail.com
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            dob=None,
            phone_number=phone_number
        )

        user.is_admin=True
        user.is_active=True
        user.is_staff=True
        user.is_superadmin=True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    username=models.CharField(max_length=50,unique=True)
    email=models.EmailField(max_length=100,unique=True)
    phone_number=models.CharField(max_length=50,blank=True,null=True)
    dob=models.DateField(null=True)


    #required
    date_joined=models.DateTimeField(auto_now_add=True)
    last_login=models.DateTimeField(auto_now_add=True)
    is_admin= models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    is_superadmin=models.BooleanField(default=False)
    # Roles Description
    is_faculty=models.BooleanField(default=False)
    is_student=models.BooleanField(default=True)
    is_hod=models.BooleanField(default=False)
    is_director=models.BooleanField(default=False)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username','first_name','last_name','phone_number']

    objects=MyAccountManager()

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,add_label):
        return True

class UserProfile(models.Model):
    COUNTRY={
    ('India','India'),
    }
    user=models.OneToOneField(Account,on_delete=models.CASCADE)
    city=models.CharField(max_length=10, blank=True,null=True)
    reg_no=models.CharField(blank=True,max_length=100,null=True)
    state=models.CharField(max_length=15, blank=True,null=True)
    country=models.CharField(max_length=10,choices=COUNTRY, default ='India', blank=True,null=True)
    qr_code=models.ImageField(blank=True , upload_to='qr_codes')

    def __str__(self):
        return self.user.first_name

    def save(self,*args,**kwargs):
        qrcode_img=qrcode.make(self.reg_no)
        canvas=Image.new('RGB',(290,290),'white')
        draw=ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname=f'qr_code-{self.reg_no}'+'.png'
        buffer=BytesIO()
        canvas.save(buffer,'PNG')
        self.qr_code.save(fname,File(buffer),save=False)
        canvas.close()
        super().save(*args,**kwargs)




class department(models.Model):
    departments={
    ('Information Technology','Information Technology'),
    ('Computer Science','Computer Science'),
    ('Mechanical','Mechanical'),
    ('Chemical','Chemical'),
    ('Civil','Civil'),
    ('Electronics','Electronics'),
    }
    department_name=models.CharField(max_length=300,choices=departments,blank=False,null=False )
    department_HOD=models.ForeignKey(Account,on_delete=models.CASCADE,limit_choices_to={'is_faculty': True},blank=True,null=True )
    datetime=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    def __str__(self):
        return self.department_name


class hod(models.Model):
    department=models.ForeignKey(department,on_delete=models.DO_NOTHING   )
    datetime=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    user=models.ForeignKey(Account,on_delete=models.CASCADE,limit_choices_to={'is_hod': True})
    def __str__(self):
        return str(self.user.username) +" "+ self.department.department_name
class faculty(models.Model):
    department=models.ForeignKey(department,on_delete=models.DO_NOTHING   )
    datetime=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    user=models.ForeignKey(Account,on_delete=models.CASCADE,limit_choices_to={'is_faculty': True})
    def __str__(self):
        return str(self.user.username) +" "+ self.department.department_name

class student(models.Model):
    year={
    ('1st Year','1st Year'),
    ('2nd Year','2nd Year'),
    ('3rd Year','3rd Year'),
    ('4th Year','4th Year'),
    }
    year=models.CharField(max_length=300,choices=year,blank=False,null=False )
    department=models.ForeignKey(department,on_delete=models.DO_NOTHING )
    user=models.ForeignKey(Account,on_delete=models.DO_NOTHING,limit_choices_to={'is_student': True})
    datetime=models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return str(self.user.username)

class Notice(models.Model):
    published_to_yr={
    ('1st Year','1st Year'),
    ('2nd Year','2nd Year'),
    ('3rd Year','3rd Year'),
    ('4th Year','4th Year'),
    }
    published_by_hod=models.ForeignKey(hod,on_delete=models.CASCADE)
    published_by_director=models.ForeignKey(Account,on_delete=models.CASCADE,limit_choices_to={'is_director': True})
    datetime=models.DateTimeField(auto_now_add=True,null=True,blank=True)

    department=models.ForeignKey(department,on_delete=models.DO_NOTHING )
    # by Director or HOD
    is_by_hod=models.BooleanField(default=False)
    is_by_director=models.BooleanField(default=False)

    # by director or hod
    is_for_department=models.BooleanField(default=False)
    is_for_all_students=models.BooleanField(default=False)
    is_for_all_faculties=models.BooleanField(default=False)


class application(models.Model):
    status_all={
    ('Submited','Submited'),
    ('Accepted','Accepted'),
    ('Accepted','Accepted'),
    ('Approoved','Approoved'),
    ('Rejected','Rejected')
    }
    status=models.CharField(max_length=1000,choices=status_all,null=True,blank=True)
    title=models.CharField(max_length=500,null=True,blank=True)
    content=models.CharField(max_length=1000,null=True,blank=True)
    reject_reason=models.CharField(max_length=500,null=True,blank=True)

    published_by_faculty=models.ForeignKey(faculty,on_delete=models.CASCADE,null=True,blank=True)
    published_by_student=models.ForeignKey(student,on_delete=models.CASCADE,null=True,blank=True)

    datetime=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    department=models.ForeignKey(department,on_delete=models.DO_NOTHING )
    # by Director or HOD

    # is_by_hod=models.BooleanField(default=False)
    is_by_faculty=models.BooleanField(default=False)
    is_by_student=models.BooleanField(default=False)
