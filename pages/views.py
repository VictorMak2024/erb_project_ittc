from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'title': 'Index Page Testing',}
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')

def team(request):
    return render(request, 'pages/team.html')

def victor(request):
    return render(request, 'pages/victor.html')

def tommy(request):
    return render(request, 'pages/tommy.html')

def wc(request):
    return render(request, 'pages/wc.html')