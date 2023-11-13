from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from .views import register, UserProfileView


app_name = 'users'

urlpatterns = [
  path('register/', register , name='register'),
  path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
  path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout' ),
  path('profile/', UserProfileView.as_view(), name='profile' ),

  path(
      'password-reset/', 
      auth_views.PasswordResetView.as_view(
          template_name='users/password_reset.html', 
          success_url=reverse_lazy('users:password_reset_done'),
          email_template_name='users/password_reset_email.html', 
      ),
      name='password_reset'),
  path(
      'password-reset/done/', 
      auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), 
      name='password_reset_done'),
  path(
      'password-reset/confirm/<uidb64>/<token>/', 
      auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html', success_url=reverse_lazy('users:password_reset_complete')),
      name='password_reset_confirm'),
  path(
      'password-reset/complete/', 
      auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
      name='password_reset_complete'),
]
