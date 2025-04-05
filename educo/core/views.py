from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from courses.models import Course
from .models import Activity
from django.contrib.auth.decorators import login_required
from django.utils import timezone

@login_required
def home(request: HttpRequest) -> HttpResponse:
    return render(request, 'home.html', {
        'courses': Course.objects.all(),
        'courses_count': Course.objects.count(),
        # Assuming 'date' is a field in Activity model 
        # the activities of the latest 7 days
        'activities': Activity.objects.filter(
            date__gte=timezone.now() - timezone.timedelta(days=7)
        ).order_by('-date'),
        'activities_count': Activity.objects.count(),
    })

def premium(request):
    return HttpResponse("You are a premium user!")

def test1(request):
    return render(request, 't1.html')