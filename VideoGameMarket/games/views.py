# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Game, Order
from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    games = Game.objects.order_by('pub_date')
    return render(request, 'games/home.html', {'games':games})


def gameDetails(request, game_id):
    game = Game.objects.get(pk = game_id)
    return render(request, 'games/gameDetails.html', {'game':game})

def buyGame(request, game_id)

def userOrders(request):
    orders = Order.objects.filter(user=request.user)
