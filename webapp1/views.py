from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .forms import InputForm
from webapp1.models import Post

def greet(response):
    return HttpResponse('Hi Developer, Good Morning Are you really a Developer')

#Home Page class
def loginpage(request):
    context = {'form': InputForm()}
    return render(request, 'loginpage.html', context)

def details(request,slug):
    q = Post.objects.filter(slug_iexact=slug)
    if q.exists():
        q = q.first()
    else:
        return HttpResponse('<h1>Post Not Found</h1>')
    context = {'post':q}
    return render(request, 'posts/details.html', context)


