from django.shortcuts import render

# Create your views here.

def homepage_view(request):
    """For the home page."""
    return render(request, 'home.html')
