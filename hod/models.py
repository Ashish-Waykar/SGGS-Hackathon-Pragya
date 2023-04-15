from django.db import models

# Create your models here.
from faculty.models import *
from authentication.models import *
from applications.models import *
from notices.models import *
from student.models import *
from director.models import *

class department(models.Model):
    departments={
    ('Information Technology','Information Technology'),
    ('Computer Science','Computer Science'),
    ('Mechanical','Mechanical'),
    ('Chemical','Chemical'),
    ('Civil','Civil'),
    ('Electronics','Electronics'),
    ('Production','Production'),
    ('Textile','Textile')
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
