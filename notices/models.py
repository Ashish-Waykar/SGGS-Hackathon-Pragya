from django.db import models

# Create your models here.

# Create your models here.
from faculty.models import *
from authentication.models import *
from applications.models import *
from hod.models import *
from student.models import *
from director.models import *

class Notice(models.Model):
    published_to_yr={
    ('1st Year','1st Year'),
    ('2nd Year','2nd Year'),
    ('3rd Year','3rd Year'),
    ('4th Year','4th Year'),
    }
    from_head={
    ('HOD','HOD'),
    ('Director','Director')
    }
    for_vendor_director={
    ('Whole College(Director)','Whole College(Director)'),
    ('For Faculty(Director)','For Faculty(Director)'),
    ('For Department HOD (Director)','For Department HOD (Director)'),
    ('For Year(Director)','For Year(Director)')
    }

    for_vendor_hod={
    ('For Faculty(HOD)','For Faculty(HOD)'),
    ('For Student(HOD)','For Student(HOD)'),
    ('For Department(HOD)','For Department(HOD)')
    }

    from_head_user_by=models.CharField(choices=from_head,max_length=200,blank=True,null=True)
    for_director_to=models.CharField(choices=for_vendor_director,max_length=200,blank=True,null=True)
    from_hod_to=models.CharField(choices=for_vendor_hod,max_length=200,blank=True,null=True)
    notice_image=models.ImageField(upload_to="notice_images/",null=True,blank=True)
    publish_to_yr=models.CharField(choices=published_to_yr,max_length=200,blank=True,null=True)

    title=models.CharField(max_length=200,blank=True,null=True)
    content=models.TextField(max_length=1000,blank=True,null=True)
    department=models.ForeignKey(department,on_delete=models.DO_NOTHING )
    datetime=models.DateTimeField(auto_now_add=True,null=True,blank=True)

    published_to_user=models.ForeignKey(Account,on_delete=models.DO_NOTHING,null=True,blank=True)

    # by Director or HOD
    is_by_hod=models.BooleanField(default=False)
    is_by_director=models.BooleanField(default=False)

    # by director or hod
    is_for_department=models.BooleanField(default=False)
    is_for_all_students=models.BooleanField(default=False)
    is_for_all_faculties=models.BooleanField(default=False)
    def __str__(self):
        return  str(self.id)+"  "+ self.from_head_user_by +"  "+str(self.datetime.date())
