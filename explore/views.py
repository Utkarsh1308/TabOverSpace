from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'explore/index.html', {})

def ai(request):
    return render(request, 'explore/ai.html', {
    "subdomain": 0,
    })

def big_data_analytics(request):
    return render(request, 'explore/big_data_analytics.html', {
    "subdomain": 2,
    })

def bioinformatics(request):
    return render(request, 'explore/bioinformatics.html', {
    "subdomain": 3,
    })

def cryptography(request):
    return render(request, 'explore/cryptography.html', {
    "subdomain": 5,
    })

def cyber_security(request):
    return render(request, 'explore/cyber_security.html', {
    "subdomain": 1,
    })

def machine_learning(request):
    return render(request, 'explore/machine_learning.html', {
    "subdomain": 4,
    })
