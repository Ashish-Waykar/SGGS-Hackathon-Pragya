from django.db import models

# Create your models here.

# Create your models here.
from faculty.models import *
from authentication.models import *
from applications.models import *
from notices.models import *
from hod.models import *
from director.models import *

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
