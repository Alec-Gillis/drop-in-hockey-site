from django.shortcuts import render
from django.utils import timezone 

from .models import Player, HeaderText

# Create your views here.
def index(request):
    all_skaters = Player.objects.filter(is_goalie=False, is_substitute=False)
    all_goalies = Player.objects.filter(is_goalie=True)
    all_subs = Player.objects.filter(is_substitute=True)
    headertext = HeaderText.objects.first()
    context = {
        'all_skaters': all_skaters,
        'all_goalies': all_goalies,
        'all_subs': all_subs,
        'headertext': headertext,
    }
    if request.method == "POST":
        everyone = Player.objects.all()
        id_list = request.POST.getlist('player')
        for x in everyone:
            if str(x.id) not in id_list:
                Player.objects.filter(pk=int(x.id)).update(is_checked_in=False)
        # Update the DB
        for x in id_list:
            player = Player.objects.filter(pk=int(x))
            if not player[0].is_checked_in:
                player.update(is_checked_in=True, time_checked_in=str(timezone.now()))

    return render(request, 'roster/index.html', context)

