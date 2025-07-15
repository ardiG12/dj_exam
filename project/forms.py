from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from project.models import CustomUser, Profile, Book


class UserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author','description','publish_year']
