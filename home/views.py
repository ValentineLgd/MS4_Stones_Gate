from django.shortcuts import render

# Create your views here.

def index(request):
    """ View returning the index page """
    return render(request, 'home/index.html')