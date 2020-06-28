from django.shortcuts import render, HttpResponse
from .forms import *
from django.views.decorators.http import require_POST


# Create your views here.

def index(request):
    form = RegisterForm()
    return render(request,
                  'index.html', {'form': form})


@require_POST
def register(request):
    form = RegisterForm(request.POST)
    if form.is_valid():
        return HttpResponse('Thank, pls check your mail')
    return render(request, 'index.html', {'form': form})
