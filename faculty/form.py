from django import forms
from .models import *
from applications.models import *
class CreateApplicationForm(forms.ModelForm):
    class Meta:
        model= application
        fields = [ 'category','title','content']
