from django.shortcuts import render, get_object_or_404
from teaminfo.models import Teams

# Create your views here.
def teaminfo(request):

    context = {
        
       'teams': Teams.objects.all(),
        
    }
    return render(request, 'teaminfo/teaminfo.html', context)


def teaminfo_detail(request, team_id):
    
     team = get_object_or_404( Teams,pk=team_id)
     context = {'team': team}
     return render(request, 'teaminfo/teamdetail.html', context)
