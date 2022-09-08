from lzma import is_check_supported
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from .models import Player


def index(request):
    skaters_count = Player.objects.filter(is_checked_in=True)
    all_skaters = Player.objects.filter(is_goalie=False)
    all_goalies = Player.objects.filter(is_goalie=True)
    context = {
        'skaters_count': skaters_count,
        'all_skaters': all_skaters,
        'all_goalies': all_goalies,
    }
    print("Request Method: " + request.method)
    if request.method == "POST":
        print("STUFF: ", request.POST)
        all_skaters.update(is_checked_in=False)
        id_list = request.POST.getlist('player')
        # Uncheck all players
        print(id_list)
        # Update the DB
        for x in id_list:
            Player.objects.filter(pk=int(x)).update(is_checked_in=True)
    return render(request, 'roster/index.html', context)

