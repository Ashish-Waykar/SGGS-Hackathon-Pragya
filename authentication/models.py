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
