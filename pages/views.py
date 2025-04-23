from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'title': 'Index Page Testing',}
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')

