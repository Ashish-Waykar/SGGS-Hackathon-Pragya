from django import forms
from .models import Account , UserProfile
class RegistrationForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput(attrs={
    'placeholder':'Enter Password',
    'id' :'registerPassword',
    'class':'input-psswd form-control',
    'autocomplete':'off',
    }))

    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
    'placeholder':'Confirm Password',
    'autocomplete':'off',
    }))

    first_name= forms.CharField(widget=forms.TextInput(attrs={
    'autocomplete':'off',
    }))
    dept= forms.CharField(widget=forms.TextInput(attrs={
    'autocomplete':'off',
    }))
    year= forms.CharField(widget=forms.TextInput(attrs={
    'autocomplete':'off',
    }))
    # dob = forms.DateField(required=False, input_formats='%d/%m/%Y')
    last_name = forms.CharField(widget=forms.TextInput(attrs={
    'autocomplete':'off',
    }))
    phone_number = forms.CharField(widget=forms.NumberInput(attrs={
    'autocomplete':'off',
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
    'autocomplete':'off',
    }))
    class Meta :
        model=Account
        fields=['first_name','last_name','phone_number','email','dob','dept','year','password']


    def clean(self):
        cleaned_data = super(RegistrationForm,self).clean()
        password=cleaned_data.get('password')
        confirm_password=cleaned_data.get('confirm_password')

        if password !=confirm_password:
            raise forms.ValidationError(
                "password Does Not Match !"
            )


    def __init__(self,*args,**kwargs):
        super(RegistrationForm,self).__init__(*args,**kwargs)
        self.fields['first_name'].widget.attrs['placeholder']='First_Name'
        self.fields['last_name'].widget.attrs['placeholder']='Last_Name'
        self.fields['first_name'].label = "First Name "
        self.fields['last_name'].label = "Last Name "

        self.fields['phone_number'].widget.attrs['placeholder']='Phone_Number'
        self.fields['phone_number'].label = "Phone Number "

        self.fields['email'].widget.attrs['placeholder']='your_reg_id@sggs.ac.in'
        self.fields['email'].label = "Email  "

        self.fields['dob'].widget.input_type='date'
        self.fields['dob'].label = "Date Of Birth "
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'


class UserForm(forms.ModelForm):
    class Meta:
        model = Account
        fields=['first_name', 'last_name','phone_number']

    def __init__(self,*args,**kwargs):
        super(UserForm,self).__init__(*args,**kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control input_text'


class UserProfileForm(forms.ModelForm):
    class Meta:
        model= UserProfile
        fields = ['reg_no','city','state','country','qr_code',]

    def __init__(self,*args,**kwargs):
        super(UserProfileForm,self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control input_text'
