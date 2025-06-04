from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('roulette/', views.roulette_view, name='roulette'),
    path('logout/', views.logout_view, name='logout'),
]