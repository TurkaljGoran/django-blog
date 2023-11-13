from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import Profile

class RegisterForm(UserCreationForm):
    
   class Meta:
      model = User
      fields = ['username', 'email']



class UserUpdateForm(forms.ModelForm):


   class Meta:
      """
      Creating a ModelForm without either the 'fields' attribute or the 'exclude' attribute is prohibited
      We use 'fields' attribute because there's way too many fields in User model to 'exclude' them 
      """

      model = User
      fields = ['username', 'email']
   

class ProfileUpdateForm(forms.ModelForm):
   
   class Meta:
      model = Profile
      fields = ['avatar']
      