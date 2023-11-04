from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('authorization',views.authorization, name = 'authorization')
]
