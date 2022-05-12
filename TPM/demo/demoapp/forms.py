from django import forms
from django.core  import validators
from demoapp.models import Organisation,Admin,Manager,Department,Employee,Task,Client,Work,UserProfileInfo
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Organisation_form(forms.ModelForm):
     class Meta:
        model =  Organisation
        fields = '__all__'

    



class Admin_form(forms.ModelForm):
    class Meta:
        model = Admin
        fields = '__all__'   






class Manager_form(forms.ModelForm):
    class Meta:    
       model = Manager
       fields = '__all__' 






class Client_form(forms.ModelForm):
    class Meta:    
        model = Client
        fields = '__all__' 






class Employee_form(forms.ModelForm):
    class Meta:
           model = Employee
           fields = '__all__' 






class Task_form(forms.ModelForm):
    class Meta:
         model = Task
         fields = '__all__' 






class Work_form(forms.ModelForm):
    class Meta:
           model = Work
           fields = '__all__' 





class Department_form(forms.ModelForm):
    class Meta:
           model = Department
           fields = '__all__' 




class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('profile_pic','portfolio_site')

  

