from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    """ A View to return Index page """

    return render(request, 'home/index.html')
