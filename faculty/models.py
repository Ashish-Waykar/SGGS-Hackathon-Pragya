from django.db import models

# Create your models here.

# Create your models here.
from authentication.models import *

from notices.models import *
from hod.models import *
from student.models import *
from director.models import *

class faculty(models.Model):
    department=models.ForeignKey(department,on_delete=models.DO_NOTHING   )
    datetime=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    user=models.ForeignKey(Account,on_delete=models.CASCADE,limit_choices_to={'is_faculty': True})
    def __str__(self):
        return str(self.user.username) +" "+ self.department.department_name
