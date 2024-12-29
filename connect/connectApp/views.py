from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello World")

def second_page(request):
    return HttpResponse("we did it!")