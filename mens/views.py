from django.shortcuts import render

# Create your views here.

def mens(request):
    return render(request, 'mens/home.html')