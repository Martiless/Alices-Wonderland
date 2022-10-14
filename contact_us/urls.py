from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContactUsView.as_view(), name='contact_us'),
    path('sign_up/', views.SignUpView.as_view(), name='sign_up'),
]
