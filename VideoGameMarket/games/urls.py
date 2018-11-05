from django.conf.urls import url
from . import views

app_name = 'games'

urlpatterns = [
    url(r'^gameDetails/(?P<game_id>[0-9]+)/$', views.gameDetails, name = 'gameDetails'),
]
