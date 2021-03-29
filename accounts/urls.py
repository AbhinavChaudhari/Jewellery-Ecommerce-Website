
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_view
from .forms import *

# LOGIN_REDIRECT_URL ='/profile',   if you wanna 
# redirect after login  put this in setting.py

# to show reset password link in terminal
# EMAIL_BACKEND ='django.core.mail.backends.console.EmailBackend'

urlpatterns = [
    
    # register urls 
    path('register/',CustomerRegistraitonView.as_view(),name='register'),

    # login urls 
    path('accounts/login/',auth_view.LoginView.as_view(template_name='login/login.html',authentication_form=LoginForm),name='login'),

    # logout urls
    path('logout/',auth_view.LogoutView.as_view(next_page='login'),name='logout'),

    # password change urls 
    path('passwordchange/',auth_view.PasswordChangeView.as_view(template_name='passwordchange/passwordchange.html',form_class=MyPassChangeForm ,success_url="/passwordchange/done/"),name='passwordchange'),

    path('passwordchange/done/',auth_view.PasswordChangeDoneView.as_view(template_name='passwordchange/passwordchangedone.html'),name='passwordchangedone'),


    # password reset urls 
    path('password-reset/',auth_view.PasswordResetView.as_view(template_name='resetpassword/password_reset.html', form_class=MyPasswordResetForm),name='password_reset'),

    path('password-reset/done/',auth_view.PasswordResetDoneView.as_view(template_name='resetpassword/password_reset_done.html'),name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>',auth_view.PasswordResetConfirmView.as_view(template_name='resetpassword/password_reset_confirm.html',form_class=MySetPassword),name='password_reset_confirm'),

    path('password-reset-complete',auth_view.PasswordResetCompleteView.as_view(template_name='resetpassword/password_reset_complete.html',),name='password_reset_complete'),


   
]
