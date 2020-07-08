from django import forms
from django.contrib.auth import models
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:

        model = CustomUser

        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'user_type'
        )


class CustomUserChangeForm(UserChangeForm):

    class Meta:

        model = CustomUser

        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'user_type'
        )




