from django.urls import path
from . import views

app_name="practice"

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:track>/<slug:subdomain>/', views.subdomain, name='subdomain'),
    path('<slug:track>/<slug:subdomain>/<slug:question>', views.question, name='question'),
]
