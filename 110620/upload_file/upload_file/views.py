from django.shortcuts import render, redirect, HttpResponse
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage()


def index(request):
    return render(request, 'index.html')


def upload(request):
    if request.method == 'POST':
        img = request.FILES.get('img')
        if img and img.name:
            saved_path = fs.save('static/' + img.name, img)
            return redirect('/' + saved_path)
    return HttpResponse('no file')
