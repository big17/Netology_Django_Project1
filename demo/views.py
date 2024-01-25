from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def hello_view(request):
    print("here1")
    print("here2")
    return HttpResponse("Hello, World");


def sum_view(request, op1, op2):
    result = op1 + op2
    return HttpResponse(result);


    

