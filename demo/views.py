from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator

# Create your views here.


def hello_view(request):
    context ={
        'test': 5,
        'data': [1, 5, 8],
        'val': 'hello',
    }
    return render(request, 'demo.html', context)


def sum_view(request, op1, op2):
    result = op1 + op2
    return HttpResponse(result);


CONTENT = [str(i) for i in range(10000)]

def pagi_view(request):
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(CONTENT, 10)
    page = paginator.get_page(page_number)
    context = {
        'page': page
    }
    return render(request, 'pagi.html', context)



