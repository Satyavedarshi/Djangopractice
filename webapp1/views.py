from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .forms import InputForm

def greet(response):
    return HttpResponse('Hi Developer, Good Morning Are you really a Developer')

#Home Page class
def loginpage(request):
    context = {'form': InputForm()}
    return render(request, 'loginpage.html', context)

