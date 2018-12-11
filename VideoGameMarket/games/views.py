# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Game, Order
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.utils import timezone

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
    else:
        searchQuery = ''
    games = Game.objects.raw('Select * FROM games_game WHERE title LIKE "%'+searchQuery+'%"')
    return render(request, 'games/search.html', {'games':games, 'searchQuery':searchQuery})

def purchaseGame(request,game_id):
    #need to check that user is logged in if request.user.is_authenticated():
    if request.user.is_authenticated:
        game = Game.objects.get(pk =game_id)
        order = Order(pub_date = timezone.datetime.now(), buyer = request.user,game = game)
        order.save()
        return home(request)
    else:
        games = Game.objects.order_by('pub_date')
        return render(request, 'games/home.html', {'games':games, 'error': 'You need to be logged in to purchase a game'})

def accountSettings(request):
    return render(request, 'games/account.html',{'name':request.user.username})


def orderHistory(request):
    orders = Order.objects.filter( buyer = request.user.id)
    games = []
    total = 0
    for order in orders:
        game = Game.objects.get(pk = order.game_id)
        game.pub_date = order.pub_date
        total+= game.price
        games.append(game)
    if total != 0:
        return render(request, 'games/orderHistory.html', {'games':games, 'total':total})
    else:
        return render(request, 'games/orderHistory.html', {'games':games})
