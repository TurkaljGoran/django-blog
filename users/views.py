from django.conf import settings
from django.views import generic, View
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect

from .forms import RegisterForm
from .forms import RegisterForm, UserUpdateForm, ProfileUpdateForm




class UserProfileView(View):

   
    def get(self, request):
        

        user: User  = request.user
        user_update_form = UserUpdateForm(instance=user)
        profile_form = ProfileUpdateForm(instance=user.profile)
       
        #RAW approach of protecting routes
        if not user.is_authenticated:
            return HttpResponseRedirect(f"{reverse_lazy(settings.LOGIN_URL)}?next={request.path}")
        return render(request, 'users/profile.html', {'user_update_form': user_update_form, 'profile_form': profile_form})


    def post(self, request):

        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_update_form.is_valid() and profile_form.is_valid():
           
           user_update_form.save()
           profile_form.save()

           messages.success(request, "Successfully updated!")

           # redirect to a success URL
           return HttpResponseRedirect(reverse_lazy('users:profile'))
        
        else:
            user_update_form = UserUpdateForm()
            profile_form = ProfileUpdateForm()
            return render(request, 'users/profile.html', {'user_update_form': user_update_form, 'profile_form': profile_form})






def register(request: HttpRequest):

    """
    if POST is empty, form will be empty, but if error happens during POST, we'll get 
    filled form back

    """
   
    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():
    
           form.save() 
           username = form.cleaned_data.get('username')
           messages.success(request, f"Your account has been created {username}, you are able to login!")
           
           # redirect to a success URL
           return HttpResponseRedirect(reverse_lazy('users:login'))
        
        else:
           return render(request, 'users/register.html', {'form': form})

    else:
        form = RegisterForm()
        return render(request, 'users/register.html', {'form': form})
    
    
    