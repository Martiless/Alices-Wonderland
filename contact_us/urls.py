from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContactUsView, name='contact_us'),
    path('', views.SignUpView, name='sign_up'),
]
