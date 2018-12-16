from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
def index(request):
    return render(request, 'practice/index.html', {})

def algorithms(request):
    return render(request, 'practice/algorithms.html', {})

def algorithms1(request):
    return render(request, 'practice/algorithms1.html', {})

def data_structures(request):
    return render(request, 'practice/data_structures.html', {})

def python(request):
    return render(request, 'practice/python.html', {})

def java(request):
    return render(request, 'practice/java.html', {})

def c(request):
    return render(request, 'practice/c.html', {})

def codemirror(request):
    return render(request, 'practice/codemirror.html', {})

def solution(request):
    if request.method == 'POST':
        url = request.POST.get('url')
    return render(request, 'practice/solution.html', {
    "url":url
    })
