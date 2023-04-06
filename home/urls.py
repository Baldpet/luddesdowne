from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact-us', views.contact, name='contact'),
    path('fixtures', views.fixtures, name='fixtures'),

]