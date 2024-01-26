from django.shortcuts import render
from django.http import HttpResponse

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


    

