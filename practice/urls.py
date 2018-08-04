from django.urls import path
from . import views

app_name="practice"

urlpatterns = [

    path('', views.index, name='index'),
    path('algorithms', views.algorithms, name='algorithms'),
    path('algorithms1', views.algorithms1, name='algorithms1'),
    path('data_structures', views.data_structures, name='data_structures'),
    path('programming_languages', views.programming_languages, name='programming_languages'),
    path('codemirror', views.codemirror, name='codemirror'),
    path('solution', views.solution, name='solution'),

]
