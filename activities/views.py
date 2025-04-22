from django.shortcuts import render, get_object_or_404
from .models import Activity

# Create your views here.
def activities(request):
    activities = Activity.objects.all()
    context = {'activities' : activities}
    return render(request, 'activities/activities.html', context)


def activity(request, activity_id):
    activity = get_object_or_404(Activity, pk=activity_id)
    activity.total_sit = activity.total_sit - activity.onenquiry_sit
    context = {'activity' : activity}
    return render(request, 'activities/activity.html', context)
