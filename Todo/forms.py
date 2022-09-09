from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import FileInput,TextInput,EmailInput,Select,Textarea,CheckboxInput,PasswordInput


class TodoForm(forms.ModelForm):
  completed = forms.BooleanField(required=False,label="Mark Completed",widget=forms.CheckboxInput(attrs={'class':'form-check-input'}))
  class Meta:
    model = Todo
    fields = ['title','description','completed']
    labels = {'title':'Task Title'}
    widgets = {
      'title':TextInput(attrs={
        'class':'form-control',
        'placeholder':'Enter title'
          }),
          'description':Textarea(attrs={
        'class':'form-control',
        'rows':'12',
        'placeholder':'Describe your Task'
      }),
        }
   
  
class RegisterForm(UserCreationForm):
  first_name = forms.CharField(required=True,label="First Name*",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'John'}))
  last_name = forms.CharField(required=True,label="Last Name*",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Doe'}))
  username = forms.CharField(required=True,label="Username*",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter a suitable username'}))
  email = forms.CharField(required=True,help_text="Enter a valid email",label="Email Address*",widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'example@gmail.com'}))
  password1 = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}))
  password2 = forms.CharField(label="Confirm Password",widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Passwords must match'}))
  class Meta:
    model = User
    fields = ['first_name','last_name','username','email','password1','password2']
 
 
class UserProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = '__all__'
    exclude = ['user']
    labels = {'avatar':'Change Profile','bio':'About Me'}
    widgets = {
      'bio':Textarea(attrs={
        'class':'form-control',
        'rows':'10',
        'placeholder':'Say more about yourself...'
      }),
      'avatar':FileInput(attrs={
        'class':'form-control',
      })
    }
    
    
class UserUpdateForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['username','email']
    widgets = {
      'username':TextInput(attrs={'class':'form-control'}),
      
      'email':EmailInput(attrs={'class':'form-control','w':'25'}),
    }