from django.urls import path
from . import views

urlpatterns = [
    path('ladies', views.ladies, name='ladies'),
]