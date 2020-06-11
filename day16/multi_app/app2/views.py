from django.shortcuts import render, HttpResponse


# Create your views here.
def hello1(request):
    return HttpResponse('hello1 from app 2')


def hello2(request):
    return HttpResponse('hello2 from app 2')
