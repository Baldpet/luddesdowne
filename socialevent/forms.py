from django import forms
from django.forms import ModelForm

from socialevent.models import Events, EventImage

class EventsForm(ModelForm):
    class Meta:
        model = Events
        fields = '__all__'
        labels = {
            'name': 'Event Name',
            'image_location': 'Image'
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': "form-control"
                }),
            'location': forms.TextInput(attrs={
                'class': "form-control"
                }),

            'image_location': forms.Select( attrs={
                'class': "form-control"
                }),
            'date': forms.DateInput(attrs={
                'class': "form-control",
                'type': 'date'
                }),
            'description': forms.Textarea(attrs={
                'class': "form-control",
                'rows': 4
                })
        }
