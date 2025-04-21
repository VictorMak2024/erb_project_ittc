from django.shortcuts import render

# Create your views here.

def supportresources(request):
    return render(request, 'supportresources/supportresources.html')