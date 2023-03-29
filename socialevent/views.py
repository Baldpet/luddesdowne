from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Events, EventImage
from .forms import EventsForm
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

@login_required
@permission_required('socialevent.add_events')
def socialevent(request):
    events = Events.objects.all().order_by('date')
    event_image = EventImage.objects.all()

    if request.method == 'POST':
        form = EventsForm(request.POST)
        if form.is_valid():
            new_event = form.save()
            return HttpResponseRedirect('/socialevent')
    else:
        form = EventsForm()
    template = 'socialevent/index.html'
    context = {
        'events': events,
        'event_image': event_image,
        'form': form
    }
    return render(request, template, context)


@login_required
@permission_required('socialevent.add_events')
def edit_socialevent(request, event_id):
    event = get_object_or_404(Events, pk=event_id)
    event_image = EventImage.objects.all()

    if request.method == "POST":
        form = EventsForm(request.POST, instance=event)
        form.save()
        return redirect('socialevent')
    else:
        form = EventsForm(instance=event)
    template = 'socialevent/edit.html'
    context = {
        'form': form,
        'event_image': event_image,
        'event': event
    }
    return render(request, template, context)


@login_required
@permission_required('socialevent.add_events')
def delete_socialevent(request, event_id):
    event = get_object_or_404(Events, pk=event_id)
    event.delete()
    return redirect('socialevent')