from django.shortcuts import render, get_object_or_404
from newsevents.models import Newsevents
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

# Create your views here.
def newsevents(request):
    newsevents=Newsevents.objects.order_by('-post_date')
     
    context = {
        
        'newsevents': newsevents,         
        
    }
    return render(request, 'newsevents/newsevents.html',context)
def newsevents_detail(request, news_id):
    newsevent= get_object_or_404(Newsevents, pk=news_id)
    context = {'newsevent': newsevent}
    return render(request, 'newsevents/newsevents_detail.html',context)
def search_news(request):
    queryset_list = Newsevents.objects.order_by('-post_date')
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(
                Q(detail__icontains=keywords) 
                |Q(title__icontains=keywords)|Q(location__icontains=keywords)
            )
    if 'news' in request.GET:
        news = request.GET['news']
        if news:
            queryset_list = queryset_list.filter(
                Q(is_News__icontains=news)
            )
    if 'events' in request.GET:
        events = request.GET['events']
        if events:
            queryset_list = queryset_list.filter(
                Q(is_Events__icontains=events)
   
            )
    if 'post_date' in request.GET:
        post_date = request.GET['post_date']
        if post_date:
            queryset_list = queryset_list.filter(
                Q(post_date__gte=post_date)
            )
    context = {
       
       'newsevents': queryset_list,
        
    }
    return render(request, 'newsevents/newsevents.html',context)