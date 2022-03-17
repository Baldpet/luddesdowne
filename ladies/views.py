from django.shortcuts import render

# Create your views here.

def ladies(request):
    return render(request, 'ladies/home.html')