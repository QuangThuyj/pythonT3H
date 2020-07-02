from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponseRedirect


# Create your views here.


def index(request):
    name = request.GET.get('name', '')
    if name:
        request.session['name'] = name
        return redirect('page2')
    return render(request, 'index.html')


def page2(request):
    name = request.GET.get('name')
    return render(request, 'page2.html', {'name': name})
