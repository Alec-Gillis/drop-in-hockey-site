from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import Player


def index(request):
    all_players = Player.objects.all()
    template = loader.get_template('roster/index.html')
    context = {
        'all_players': all_players
    }
    return HttpResponse(template.render(context, request))

