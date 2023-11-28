from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name = 'authentication'),
    path('registration', views.registration, name = 'registration'),
]
