from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('list_categoty', listCategory),
    path('add_category', addCategory),
]