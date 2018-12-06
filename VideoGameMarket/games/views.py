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

def search(request):
    if request.method == "POST":
        searchQuery = request.POST['search'] 
        games = Game.objects.raw('Select * FROM games_game WHERE title LIKE "%'+searchQuery+'%"')
    else:
        games = Game.objects.raw('Select * FROM games_game WHERE title LIKE "%mario%"')

    return render(request, 'games/search.html', {'games':games})
