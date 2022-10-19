from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_contact_us_form, name='contact_us'),
    path('sign_up/', views.get_sign_up_form, name='sign_up'),
]
