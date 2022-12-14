from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about_me/', views.about_me, name='about_me'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
]
