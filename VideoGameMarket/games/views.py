# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Game, Order
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import datetime


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

def purchaseGame(request,game_id):
    #need to check that user is logged in if request.user.is_authenticated():
    if request.user.is_authenticated:
        order = Order()
        order.pub_date = datetime.datetime.now()
        order.save()
        order.buyer.set([request.user.id])
        order.game.set([game_id])
        return home(request)
    else:
        return home(request,{'error': 'You need to be logged in to purchase a game'})



def orderHistory(request):
    order = Order.objects.filter(buyer = request.user.id)
    games = Order.objects.raw('Select game_id FROM games_order WHERE user_id = '+ str(request.user.id))
    return render(request, 'games/search.html', {'games':games})
