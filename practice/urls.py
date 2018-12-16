from django.urls import path
from . import views

app_name="practice"

urlpatterns = [
    #below six belong to algorithms
    path('', views.index, name='index'),
    path('algorithms/algorithms.html', views.algorithms, name='algorithms'),
    path('algorithms/greedy_algorithms/greedy_algorithms.html', views.greedy_algorithms, name='greedy_algorithms'),
    path('algorithms/string_algorithms/string_algorithms.html', views.string_algorithms, name='string_algorithms'),
    path('algorithms/sorting/sorting.html', views.sorting, name='sorting'),
    path('algorithms/dynamic_programming/dynamic_programming.html', views.dynamic_programming, name='dynamic_programming'),
    path('algorithms/dynamic_programming/questions/Sherlock and Coprime Subset.html', views.sherlock, name='sherlock'),
    path('algorithms/graphs/graphs.html', views.graphs, name='graphs'),
    
    
    path('algorithms/dynamic_programming/questions/Simulation.html', views.sim, name='sim'),
    path('algorithms/dynamic_programming/questions/Explore.html', views.exp, name='exp'),

    path('data_structures', views.data_structures, name='data_structures')
]
