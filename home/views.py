from django.shortcuts import render
from socialevent.models import Events
from datetime import date

# Create your views here.

def home(request):
    today = date.today()
    events = Events.objects.exclude(date__lt=today).order_by('date')[:3]
    context = {
        'events': events
    }
    return render(request, 'home/index.html', context)

def contact(request):
    return render(request, 'home/contact.html')