from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from .models import Player


def index(request):
    all_skaters = Player.objects.filter(is_goalie=False)
    all_goalies = Player.objects.filter(is_goalie=True)

    context = {
        'all_skaters': all_skaters,
        'all_goalies': all_goalies,
    }
    return render(request, 'roster/index.html', context)

