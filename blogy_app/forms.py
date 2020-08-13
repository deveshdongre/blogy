from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import Profile


class UserCreateForm(UserCreationForm):
    birthdate = forms.DateField(help_text='DOB')

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2',
                  'email', 'first_name', 'last_name', 'birthdate']
        #   "first_name", "last_name", "email", "birthdate",)

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
