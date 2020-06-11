from django.urls import path
from .views import *

urlpatterns = [
    path('hello1', hello1)
]