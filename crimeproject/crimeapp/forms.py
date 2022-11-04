
# import form class from django
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
 
# create a ModelForm
class casesform(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Reported
        fields = "__all__"
        exclude = ('Status','Penalty','CourtStatus')
    def __init__ (self, *args, **kwargs):
        super(casesform,self).__init__(*args,**kwargs)
        self.fields['Reference_Number'].widget.attrs['class']='form-control'
        self.fields['title'].widget.attrs['class']='form-control form-label'
        self.fields['description'].widget.attrs['class']='form-control'
        self.fields['personreported'].widget.attrs['class']='form-control'
        self.fields['Officerincharge'].widget.attrs['class']='form-control'
        self.fields['tribe'].widget.attrs['class']='form-control'
        self.fields['Telephone_Number'].widget.attrs['class']='form-control'
        self.fields['Residence'].widget.attrs['class']='form-control'
        self.fields['CrimeScene'].widget.attrs['class']='form-control'


class individualcasesform(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Reported
        # fields = ['title','description','personreported','tribe','Residence']
        fields="__all__"
        exclude =('Status','Officerincharge','Penalty')
        
    def __init__ (self, *args, **kwargs):
        super(individualcasesform,self).__init__(*args,**kwargs)

        self.fields['Reference_Number'].widget.attrs['class']='form-control form-label disabled'
        self.fields['title'].widget.attrs['class']='form-control form-label'
        self.fields['description'].widget.attrs['class']='form-control'
        self.fields['personreported'].widget.attrs['class']='form-control'
        self.fields['Telephone_Number'].widget.attrs['class']='form-control form-label'
        self.fields['CrimeScene'].widget.attrs['class']='form-control'
        self.fields['tribe'].widget.attrs['class']='form-control'
        self.fields['Residence'].widget.attrs['class']='form-control'


class searchForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Reported
        # fields = ['title','description','personreported','tribe','Residence']
        fields = ['title']
        # fields="__all__"
        exclude =('description','personreported','tribe','Residence', 'Officerincharge','last_modified','CrimeScene','Status','Penalty',)
        



class LoginForm(forms.Form):
    username=forms.CharField(
        widget=forms.TextInput(
            attrs={"class":"form-control"}
        )
    )

    password=forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class":"form-control"}
        )
    )

class SignupForm(UserCreationForm):
    username=forms.CharField(
        widget=forms.TextInput(
            attrs={"class":"form-control"}
        )
    )

    # firstname=forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={"class":"form-control"}
    #     )
    # )

    # lastname=forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={"class":"form-control"}
    #     )
    # )

    dutystation=forms.CharField(
        widget=forms.TextInput(
            attrs={"class":"form-control"}
        )
    )

    contact=forms.CharField(
        widget=forms.TextInput(
            attrs={"class":"form-control"}
        )
    )

    

    subcounty=forms.CharField(
        widget=forms.TextInput(
            attrs={"class":"form-control"}
        )
    )

    district=forms.CharField(
        widget=forms.TextInput(
            attrs={"class":"form-control"}
        )
    )

    email=forms.CharField(
        widget=forms.TextInput(
            attrs={"class":"form-control"}
        )
    )

    # Options = [
    #     ('Police Officer', 'Police Officer'),
    #     ('Court Officer', 'Court Officer'),
    #     ('Sub Admin', 'Sub admin'),
    #   ]
    # role = forms.ChoiceField(label='Category', widget=forms.Select, choices=Options)
    # select = forms.ChoiceField(widget=forms.Select, choices=role)

    class Meta:
        model=User
        fields=('username','first_name','last_name','email','subcounty','district','dutystation','contact','is_admin','is_police_officer','is_court_Officer')
        # fields=('username','first_name','last_name','email','subcounty','district','dutystation','contact','role')
    def __init__ (self, *args, **kwargs):
        super(SignupForm,self).__init__(*args,**kwargs)

        self.fields['first_name'].widget.attrs['class']='form-control'
        self.fields['last_name'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['class']='form-control'