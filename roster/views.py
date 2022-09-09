from django.shortcuts import render
from django.utils import timezone 

from .models import Player, HeaderText

# Create your views here.
def index(request):
    all_skaters = Player.objects.filter(is_goalie=False, is_substitute=False).order_by('name')
    all_goalies = Player.objects.filter(is_goalie=True).order_by('name')
    all_subs = Player.objects.filter(is_substitute=True).order_by('name')
    # when the user hits submit, this will update the db
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

    waiters = {}
    # regulars that are playing
    people_playing = Player.objects.filter(is_goalie=False, is_substitute=False, is_checked_in=True)
    # wait list
    wait_list = Player.objects.filter(is_goalie=False, is_substitute=True, is_checked_in=True).order_by('time_checked_in')
    while len(wait_list) and len(people_playing) < 22:
        remove_player = wait_list.first() 
        people_playing |= Player.objects.filter(pk=remove_player.id)
        wait_list = wait_list.exclude(pk=int(remove_player.id))
    waiters = wait_list.order_by('time_checked_in')

    # Determine how many people need to sign out before next person is signed in
    signout_amount = 0
    if len(all_skaters.filter(is_checked_in=True)) >= 22:
        signout_amount = len(all_skaters.filter(is_checked_in=True)) - 21
    else:
        signout_amount = 1

    headertext = HeaderText.objects.first()
    context = {
        'all_skaters': all_skaters,
        'all_goalies': all_goalies,
        'all_subs': all_subs,
        'headertext': headertext,
        'waiters': waiters,
        'signout_amount': signout_amount,
    }

    return render(request, 'roster/index.html', context)

