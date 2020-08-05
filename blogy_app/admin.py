from django.contrib import admin
from .models import UserDetail
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = UserDetail
    list_display = ['email', 'username', ]


# Register your models here.
admin.site.register(UserDetail, CustomUserAdmin)
