from django import forms
from django.contrib.auth.models import User

class SignupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']
        widgets = {
            'username': forms.TextInput(attrs={'class':'input','placeholder':'Enter Username','id':'username'}),
            'email':    forms.EmailInput(attrs={'class':'input','placeholder':'Enter Email','id':'email'}),
            'password': forms.PasswordInput(attrs={'class':'input','placeholder':'Enter Password','id':'password'})
        }

class LoginForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password']
        widgets = {
            'username': forms.TextInput(attrs={'class':'input','placeholder':'Enter Username','id':'log_username'}),
            'password': forms.PasswordInput(attrs={'class':'input','placeholder':'Enter Password','id':'log_password'})
        }