from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('page2', page2, name='page2')
]
