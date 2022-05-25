import phonenumbers
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

from .models import Profile

User = get_user_model()


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(
        required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.IntegerField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }), required=True)
    work_phone = forms.IntegerField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }), required=True)
    address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Andijon shaxri, Seramov Ko'chasi",
        'class': 'form-control',
    }), required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'first_name', 'last_name', 'work_phone', 'address']


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(
        attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 5
    }))

    class Meta:
        model = Profile
        fields = ['avatar', 'bio']


# register form here
class RegisterForm(UserCreationForm):
    # fields we want to include and customize in our form
    first_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'First Name',
            'class': 'form-control',
        }))
    last_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Last Name',
            'class': 'form-control',
        }))
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Username',
            'class': 'form-control',
        }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={
                                 'placeholder': 'Email',
                                 'class': 'form-control',
                             }))
    phone = forms.IntegerField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }), required=True)
    work_phone = forms.IntegerField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }), required=True)
    address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Andijon shaxri, Seramov Ko'chasi",
        'class': 'form-control',
    }), required=False)
    work_field = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Ex: Teacher",
        'class': 'form-control',
    }), required=False)
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(
                                    attrs={
                                        'placeholder': 'Password',
                                        'class': 'form-control',
                                        'data-toggle': 'password',
                                        'id': 'password',
                                    }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(
                                    attrs={
                                        'placeholder': 'Confirm Password',
                                        'class': 'form-control',
                                        'data-toggle': 'password',
                                        'id': 'password',
                                    }))

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'username', 'email', 'phone', 'work_phone', 'address', 'work_field', 'password1',
            'password2'
        ]


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    password = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'class': 'form-control',
                                                                 'data-toggle': 'password',
                                                                 'id': 'password',
                                                                 'name': 'password',
                                                                 }))
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']

