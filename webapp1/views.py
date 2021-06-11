from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def greet(response):
    return HttpResponse('Hi Developer, Good Morning Are you really a Developer')
