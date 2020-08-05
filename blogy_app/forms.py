from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserDetail


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = UserDetail
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = UserDetail
        fields = ('username', 'email')
