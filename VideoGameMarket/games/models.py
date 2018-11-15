# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Game(models.Model):
    title = models.CharField(max_length = 250)
    pub_date = models.DateTimeField()
    description = models.TextField()
    price = models.DecimalField(max_digits = 5, decimal_places = 2)
    image = models.ImageField(upload_to= 'media/')

    platforms_choices = (
        ('xbox', 'XBOX ONE'),
        ('playstation', 'Playstation 4'),
        ('Nintendo', 'Nintendo Switch'),
        ('PC', 'PC'),
    )
    platform = models.CharField(
        max_length=30,
        choices= platforms_choices,
        default='PC',
    )

    def __str__(self):
        return self.title

    def summary(self):
        return self.description[:60]


class Order(models.Model):
    pub_date = models.DateTimeField()
    buyer = models.ForeignKey(User)
    game =  model.ForeignKey(Game)
