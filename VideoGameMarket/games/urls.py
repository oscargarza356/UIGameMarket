from django.conf.urls import url
from . import views

app_name = 'games'

urlpatterns = [
    url(r'^search/', views.search, name = 'search'),
    url(r'^orderHistory/', views.orderHistory, name = 'orderHistory'),
    url(r'^gameDetails/(?P<game_id>[0-9]+)/$', views.gameDetails, name = 'gameDetails'),
    url(r'^purchaseGame/(?P<game_id>[0-9]+)/$', views.purchaseGame, name = 'purchaseGame'),
]
