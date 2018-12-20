from django.urls import path
from . import views

app_name="home"

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_user, name='login'),
    path('register', views.register, name='register'),
    path('leaderboard', views.leaderboard, name='leaderboard'),
    path('logout_user', views.logout_user, name='logout_user')
]
