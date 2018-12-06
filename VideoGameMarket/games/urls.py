from django.conf.urls import url
from . import views

app_name = 'games'

urlpatterns = [
    url(r'^search/', views.search, name = 'search'),
    url(r'^gameDetails/(?P<game_id>[0-9]+)/$', views.gameDetails, name = 'gameDetails'),
]
