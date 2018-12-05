# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Game
from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    games = Game.objects.order_by('pub_date')
    return render(request, 'games/home.html', {'games':games})


def gameDetails(request, game_id):
    game = Game.objects.get(pk = game_id)
    return render(request, 'games/gameDetails.html', {'game':game})
