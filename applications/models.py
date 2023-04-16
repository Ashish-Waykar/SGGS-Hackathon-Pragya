from django.db import models

# Create your models here.

# Create your models here.
from authentication.models import *
from notices.models import *
from hod.models import *
# from faculty.models import faculty
# from student.models import  student
from director.models import *

class application(models.Model):
    status_all={
    ('Submited','Submited'),
    ('Accepted Level 1','Accepted Level 1'),
    ('Approoved','Approoved'),
    ('Rejected','Rejected')
    }
    categories_all={
    ('Leave','Leave'),
    ('Request','Request'),
    ('Documents','Documents'),
    ('Other','Other')
    }
    application_id=models.CharField(max_length=100,blank=True,null=True)
    status=models.CharField(max_length=1000,choices=status_all,null=True,blank=True)
    category=models.CharField(max_length=1000,choices=categories_all,null=True,blank=True)
    title=models.CharField(max_length=500,null=True,blank=True)
    content=models.TextField(max_length=1000,null=True,blank=True)
    reject_reason=models.CharField(max_length=500,null=True,blank=True)
    publisher_user=models.ForeignKey(Account,on_delete=models.CASCADE,null=True,blank=True)
    # published_by_faculty=models.ForeignKey(faculty,on_delete=models.CASCADE,null=True,blank=True)
    # published_by_student=models.ForeignKey(student,on_delete=models.CASCADE,null=True,blank=True)

    datetime=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    department=models.ForeignKey(department,on_delete=models.DO_NOTHING )
    # by Director or HOD

    # is_by_hod=models.BooleanField(default=False)
    is_published_by_faculty=models.BooleanField(default=False)
    is_published_by_student=models.BooleanField(default=False)

    # Rejected by
    is_rejected_by_director=models.BooleanField(default=False)
    is_rejected_by_hod=models.BooleanField(default=False)
    def __str__(self):
        return self.application_id
