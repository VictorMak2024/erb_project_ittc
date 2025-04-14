from django.shortcuts import render

# Create your views here.
def newsevents(request):
    context = {}
    return render(request, 'newsevents/newsevents.html',context)
def newsevents_detail(request, news_id):
    context = {}
    return render(request, 'newsevents/newsevents_detail.html',context)
def search(request):
    context = {}
    return render(request, 'newsevents/search.html',context)