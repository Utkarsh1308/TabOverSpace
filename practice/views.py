from django.shortcuts import get_object_or_404, render

from .models import Track, Subdomain, Question

# Create your views here.
def index(request):
    return render(request, 'practice/index.html', {})

def subdomain(request, track, subdomain):

    def section(x):
        if '_' in str(x):
            sections = x.split('_')
            y = sections[0].capitalize() + " " + sections[1].capitalize()
            return y
        return x.capitalize()

    Subdomains = Subdomain.objects.all()

    section = get_object_or_404(Subdomain, name=section(subdomain), track__name=section(track))
    context = {
    'section': section,
    'Subdomains': Subdomains,
    'track': track,
    }
    return render(request, 'practice/subdomain.html', context)

def question(request, subdomain, question, track):

    return render(request, 'practice/question.html', {})
