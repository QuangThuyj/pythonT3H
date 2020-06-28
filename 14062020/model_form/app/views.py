from django.shortcuts import render
from .models import *
from .forms import CategoryForm


# Create your views here.
def index(request):
    return render(request, 'index.html')


def listCategory(request):
    category_list = Category.objects.all()
    return render(request, 'category/list.html',
                  {'category_list': category_list})


def addCategory(request):
    form = CategoryForm()
    return render(request, 'category/form.html', {'form': form})