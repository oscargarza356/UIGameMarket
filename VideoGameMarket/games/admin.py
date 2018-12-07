# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Game, Order

admin.site.register(Game)
admin.site.register(Order)

# Register your models here.
