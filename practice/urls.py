from django.urls import path
from . import views

app_name="practice"

urlpatterns = [

    path('', views.index, name='index'),
    path('data_structures', views.data_structures, name='data_structures'),
    path('algorithms/constructive_algorithms', views.constructive_algorithms, name='constructive_algorithms'),
    path('algorithms/dynamic_programming', views.dynamic_programming, name='dynamic_programming'),
    path('algorithms/graph_theory', views.graph_theory, name='graph_theory'),
    path('algorithms/greedy', views.greedy, name='greedy'),
    path('algorithms/implementation', views.implementation, name='implementation'),
    path('algorithms/np_complete', views.np_complete, name='np_complete'),
    path('algorithms/recursion', views.recursion, name='recursion'),
    path('algorithms/search', views.search, name='search'),
    path('algorithms/sorting', views.sorting, name='sorting'),
    path('algorithms/strings', views.strings, name='strings'),
    path('algorithms/warmup', views.warmup, name='warmup'),
    path('c/classes', views.classes, name='classes'),
    path('c/debugging', views.debugging, name='debugging'),
    path('c/inheritance', views.inheritance, name='inheritance'),
    path('c/introduction', views.introduction, name='introduction'),
    path('c/stl', views.stl, name='stl'),
    path('c/strings', views.strings_cpp, name='strings_cpp'),
    path('java/advanced', views.advanced, name='advanced'),
    path('java/bignumber', views.bignumber, name='bignumber'),
    path('java/data_structures', views.data_structures_java, name='data_structures_java'),
    path('java/exception_handling', views.exception_handling, name='exception_handling'),
    path('java/introduction', views.introduction_java, name='introduction_java'),
    path('java/strings', views.strings_java, name='strings_java'),
    path('python/classes', views.classes_python, name='classes_python'),
    path('python/collections', views.collections, name='collections'),
    path('python/debugging', views.debugging_python, name='debugging_python'),
    path('python/introduction', views.introduction_python, name='introduction_python'),
    path('python/itertools', views.itertools, name='itertools'),
    path('python/math', views.math, name='math'),
    path('python/numpy', views.numpy, name='numpy'),
    path('python/sets', views.sets, name='sets'),
    path('python/strings', views.strings_python, name='strings_python'),
    path('python/xml', views.xml, name='xml'),


]
