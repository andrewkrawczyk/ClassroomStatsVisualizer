"""
Definition of forms.
"""
import re

from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from .models import *


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder': 'Password'}))


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class CreateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_id', 'teacher', 'first_name', 'last_name', 'last_name', 'truancy', 'composite_score']
        widgets = {
            'student_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Student ID'}),
            'teacher': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'truancy': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Truancy'}),
            'composite_score': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'})
        }

    def clean_student_id(self):
        data = self.cleaned_data.get('student_id')
        if len(str(data)) != 8:
            raise forms.ValidationError("Student ID is not 8 digits long (0 at the start?)")

        if not re.match("[1-9][0-9]{7}", str(data)):
            raise forms.ValidationError("Student ID is not all digits or not starting with 1-9")

        return data

    def clean_first_name(self):
        data = self.cleaned_data.get('first_name')
        if len(data) < 3:
            raise forms.ValidationError("First name is not 4 character long")

        return data

    def clean_last_name(self):
        data = self.cleaned_data.get('last_name')
        if len(data) < 3:
            raise forms.ValidationError("Last name is not 4 character long")

        return data

    def clean_truancy(self):
        data = self.cleaned_data.get('truancy')
        if int(data) >= 365 or int(data) < 0:
            raise forms.ValidationError("Truancy is not a positive integer and/or less than 366")

        return data
