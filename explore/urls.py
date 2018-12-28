from django.urls import path
from . import views

app_name="explore"

urlpatterns = [
    path('', views.index, name='index'),
    path('ai', views.ai, name='ai'),
    path('big_data_analytics', views.big_data_analytics, name='big_data_analytics'),
    path('bioinformatics', views.bioinformatics, name='bioinformatics'),
    path('cryptography', views.cryptography, name='cryptography'),
    path('cyber_security', views.cyber_security, name='cyber_security'),
    path('machine_learning', views.machine_learning, name='machine_learning'),
]
