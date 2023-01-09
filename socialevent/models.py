from django.db import models
from django.forms import ModelForm
from django import forms

# Create your models here.

class Events(models.Model):
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    description = models.TextField()
    image_location = models.CharField(max_length=150)
    date = models.DateField()

    def __str__(self):
        return self.name

class EventsForm(ModelForm):
    class Meta:
        model = Events
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }