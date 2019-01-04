from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'explore/index.html', {
    "subdomain": 0,
    })
def exp_article(request):
    return render(request, 'explore/exp_article.html', {
    "subdomain": 0,
    })
