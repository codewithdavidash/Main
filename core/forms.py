from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import ApplicationModel
from django import forms

INPUT_STYLES = """
border-b border-yellow-500 w-[18rem] hover:border-yellow-800 p-1 bg-transparent
"""
APP_STYLES = """
border-b border-yellow-500 w-[18rem] lg:w-[21rem] hover:border-yellow-800 p-1 bg-transparent
"""


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': INPUT_STYLES
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': INPUT_STYLES
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': INPUT_STYLES
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': INPUT_STYLES
    }))


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': INPUT_STYLES
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': INPUT_STYLES
    }))


class AppForm(forms.ModelForm):
    class Meta:
        model = ApplicationModel
        fields = ('first_name', 'middle_name', 'last_name', 'date_of_birth', 'email',
                  'phone', 'address', 'educational_qualification', 'reason', 'cv')
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': APP_STYLES
            }),
            'middle_name': forms.TextInput(attrs={
                'class': APP_STYLES
            }),
            'last_name': forms.TextInput(attrs={
                'class': APP_STYLES
            }),
            'date_of_birth': forms.DateInput(attrs={
                'class': APP_STYLES
            }),
            'phone': forms.TextInput(attrs={
                'class': APP_STYLES
            }),
            'email': forms.EmailInput(attrs={
                'class': APP_STYLES
            }),
            'address': forms.TextInput(attrs={
                'class': APP_STYLES
            }),
            'educational_qualification': forms.TextInput(attrs={
                'class': APP_STYLES
            }),
            'reason': forms.Textarea(attrs={
                'class': 'border w-[18rem] lg:w-[21rem] lg:h-[5rem] p-1 bg-white'
            }),
            'cv': forms.FileInput(attrs={
                'class': APP_STYLES
            }),
        }
