from django.shortcuts import render, HttpResponse


# Create your views here.

def hello1(request):
    return HttpResponse('hello 1')


def hello2(request):
    return HttpResponse('hello 2')
