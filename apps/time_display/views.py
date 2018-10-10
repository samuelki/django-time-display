from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def index(request):
    context = {
        'date': strftime("%B %d, %Y"),
        'time': strftime("%I:%M %p")
    }
    return render(request, 'time_display/index.html', context)