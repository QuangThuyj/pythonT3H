from django.urls import path
from .views import *

urlpatterns = [
    path('hello1', hello1),
    path('hello2', hello2),
]