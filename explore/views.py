from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'explore/index.html', {
    "subdomain": 0,
    })
