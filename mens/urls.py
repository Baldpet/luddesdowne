from django.urls import path
from . import views

urlpatterns = [
    path('mens', views.mens, name='mens'),
]