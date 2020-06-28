from django.shortcuts import render
from .models import Student
from django.db.models import Q
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    PAGE_SIZE = 5
    keyword = request.GET.get('keyword', '')
    page = int(request.GET.get('page', 1))
    studentList = Student.objects.all()
    if keyword != '':
        studentList = studentList.filter(
            Q(studentName__contains=keyword) |
            Q(studentName__contains=keyword)
        )
    paginator = Paginator(studentList, PAGE_SIZE)
    curItems = paginator.get_page(page)
    return render(request, 'index.html',
                  {
                      'curItems': curItems,
                      'page': page,
                      'num_pages': paginator.num_pages,
                      'total': paginator.count,
                      'keyword': keyword,
                      'offset': PAGE_SIZE*(page-1)
                  })
