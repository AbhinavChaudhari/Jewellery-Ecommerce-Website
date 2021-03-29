from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.utils.translation import gettext,gettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth import password_validation

class CustomerRegistraitonForm(UserCreationForm):
    
    password1 = forms.CharField(required=True,label='Password 1',widget=forms.PasswordInput(attrs={'placeholder':"Enter Your Password"}))
    password2 = forms.CharField(required=True,label='Password 2',widget=forms.PasswordInput(attrs={'placeholder':"Enter Again Your Password"}))
    email = forms.CharField(required=True, label='Email',widget=forms.EmailInput(attrs={'placeholder':"Enter Your Email"}))
   

    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']
        labels = {'email':'Email'}
        widgets = {'username':forms.TextInput(attrs={'placeholder':'Enter Your Username'}),'first_name':forms.TextInput(attrs={'placeholder':'Enter Your firstname'}),'last_name':forms.TextInput(attrs={'placeholder':'Enter Your LastName'})}


class LoginForm(AuthenticationForm):
    username = UsernameField(label=_("Username"), widget=forms.TextInput(attrs={'autofocus':True,'placeholder':'Enter Username'}))
    password = forms.CharField(label=_("Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','placeholder':'Enter Password'}))

class MyPassChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_('Old Password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','autofocus':True ,'placeholder':"Enter Old Password"}))
    new_password1 = forms.CharField(label=_('New Password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password',"placeholder":'Enter Your New Password'}),help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_('Confirm New Password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password',"placeholder":"Confirm Password"}))


class MyPasswordResetForm(PasswordResetForm):
    email= email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email'})
    )


class MySetPassword(SetPasswordForm):
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
