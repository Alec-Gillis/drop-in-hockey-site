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
    checked_in_waiters = Player.objects.filter(is_goalie=False, is_substitute=True, is_checked_in=True)
    all_checked_in = len(checked_in_waiters) + len(all_skaters.filter(is_checked_in=True))
    wait_list = Player.objects.filter(is_goalie=False, is_substitute=True, is_checked_in=True).order_by('time_checked_in')
    while len(wait_list) and all_checked_in < 22:
        wait_list.first().update(is_checked_in=True) 
        wait_list = Player.objects.filter(is_goalie=False, is_substitute=True, is_checked_in=True).order_by('time_checked_in')
    waiters = wait_list.order_by('name')

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

