from django.shortcuts import render

# Create your views here.

def rwc_home(request):
    return render(request, 'rwc_home', {})