from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about_me/', views.about_me, name='about_me'),
]
