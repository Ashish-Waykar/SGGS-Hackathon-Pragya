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
