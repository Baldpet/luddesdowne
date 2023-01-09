from django.urls import path
from . import views

urlpatterns = [
    path('socialevent', views.socialevent, name='socialevent'),
    path('edit_event/<event_id>', views.edit_socialevent, name='edit_socialevent'),
    path('delete_event/<event_id>', views.delete_socialevent, name='delete_socialevent')
]