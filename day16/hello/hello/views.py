from django.shortcuts import HttpResponse, render


def index(request):
    return render(request, 'index.html')  # HttpResponse("hello")


def hello(request):
    name = request.GET.get('name', 'world')  # /hello?name=abc
    gender = request.GET.get('gender')
    salutation = 'Mr' if gender == 'M' else 'Mrs'
    return render(request, 'hello.html',
                  {
                      'name': name,
                      'salutation': salutation
                  })


def hello2(request):
    if request.method == 'POST':
        name = request.POST.get('name', 'world')  # /hello?name=abc
        gender = request.POST.get('gender')
        salutation = 'Mr' if gender == 'M' else 'Mrs'
        return render(request, 'hello2.html',
                      {
                          'name': name,
                          'salutation': salutation
                      })
    else:
        return HttpResponse('Method does not supported')
