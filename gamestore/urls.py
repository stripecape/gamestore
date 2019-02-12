from django.urls import path
from gamestore import views
from gamestore.views import CatalogView, MyGamesView
from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.contrib.auth.views import (
    login, logout
)

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),
    url(r'^login/$', login, {'template_name':'login.html'}, name='login'),
    #url(r'^catalog/', TemplateView.as_view(template_name="catalog.html"),
    #               name='catalog'),
    url(r'^catalog/', CatalogView.as_view(), name='catalog'),
    url(r'^gameregistration/$', views.gameregistration, name='gameregistration'),
    url(r'^game/$', views.game, name='game'),
    url(r'^mygames/', MyGamesView.as_view(), name='mygames'),
    url(r'^playgame/$', views.playgame, name='playgame'),
    url(r'^purchase/$', views.purchase, name='purchase'),
    #url(r'^catalog/$', views.get_games, name='get_games'),
]
