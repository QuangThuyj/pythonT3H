from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import *


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'phone')


class MyUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'phone')
