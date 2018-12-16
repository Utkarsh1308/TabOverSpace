from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'practice/index.html', {})

def algorithms(request):
    return render(request, 'practice/algorithms/algorithms.html', {})

#dp problems
def dynamic_programming(request):
    return render(request, 'practice/algorithms/dynamic_programming/dynamic_programming.html', {})
def sherlock(request):
    return render(request, 'practice/algorithms/dynamic_programming/questions/Sherlock and Coprime Subset.html', {})

def exp(request):
    return render(request, 'practice/algorithms/dynamic_programming/questions/Explore.html', {})


def sim(request):
    return render(request, 'practice/algorithms/dynamic_programming/questions/Simulation.html', {})



def graphs(request):
    return render(request, 'practice/algorithms/graphs/graphs.html', {})



def greedy_algorithms(request):
    return render(request, 'practice/algorithms/greedy_algorithms/greedy_algorithms.html', {})



def string_algorithms(request):
    return render(request, 'practice/algorithms/string_algorithms/string_algorithms.html', {})




def sorting(request):
    return render(request, 'practice/algorithms/sorting/sorting.html', {})


def data_structures(request):
    return render(request, 'practice/data_structures/data_structures.html', {})
