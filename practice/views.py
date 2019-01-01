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
    }
    if track == 'algorithms' and str(section.track) == 'Algorithms':
        return render(request, 'practice/subdomain.html', context)
    if track == 'data_structures' and str(section.track) == 'Data Structures':
        return render(request, 'practice/subdomain2.html', context)
    if track == 'cpp' and str(section.track) == 'Cpp':
        return render(request, 'practice/subdomain3.html', context)
    if track == 'java' and str(section.track) == 'Java':
        return render(request, 'practice/subdomain4.html', context)
    if track == 'python' and str(section.track) == 'Python':
        return render(request, 'practice/subdomain5.html', context)
