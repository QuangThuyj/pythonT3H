from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import forms, models


# Register your models here.


class MyUserAdmin(UserAdmin):
    add_form = forms.MyUserCreationForm
    form = forms.MyUserChangeForm
    model = models.User
    list_display = ['username', 'phone']


admin.site.register(models.User, MyUserAdmin)
