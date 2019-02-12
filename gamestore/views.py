from django.shortcuts import render, redirect
from .models import StoreUser, Game, AllGames, Store #UserManager
from django.contrib.auth.forms import UserCreationForm
from gamestore.forms import RegistrationForm, GameRegistrationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView
import json
from hashlib import md5



#class CatalogView(TemplateView):
#    template_name = 'templates/catalog.html'
class CatalogView(TemplateView):
    template_name = 'catalog.html'
    def get(self, request):
        allgames = AllGames.objects.all()
        args = {'allgames':allgames}
        return render(request, self.template_name, args)

def game(request):
    gameid = request.POST.__getitem__("game_id")
    game = AllGames.objects.get(id=gameid)
    user = request.user
    args = {'game':game, 'user':user}
    return render(request, "game.html", args)

def purchase(request):
    gameid = request.POST.__getitem__("game_id")
    gameprice = request.POST.__getitem__("game_price")
    pidd = gameid
    sid = "xdxachepeedzsnhs"
    secret_key = "22bb869888dc66715cf61785277bfad3"
    amount = gameprice

    checksumstr = "pid={}&sid={}&amount={}&token={}".format(pidd, sid, amount, secret_key)
    m = md5(checksumstr.encode("ascii"))
    gamepurchase = Store(pid=gameid, amount=gameprice, checksum=m.hexdigest())
    gamepurchase.save()
    args = {'gamepurchase':gamepurchase}
    return render(request, "purchase.html", args)

def playgame(request):
    gameid = request.POST.__getitem__("game_id")
    game = AllGames.objects.get(id=gameid)
    args = {'game':game}
    return render(request, "playgame.html", args)

class MyGamesView(TemplateView):
    template_name = 'mygames.html'
    def get(self, request):
        mygames = Game.objects.all()
        args = {'mygames':mygames}
        return render(request, self.template_name, args)

def get_games(request):
        allgames = AllGames.objects.all()
        args = {'allgames':allgames}
        return render(request, "catalog.html", args)

def home(request):
    storeusers = StoreUser.objects.all()
    args = {'storeusers':storeusers}
    return render(request, "frontpage.html", args)

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.storeuser.developer = form.cleaned_data.get('developer')
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(home)
            #return HttpResponseRedirect(home)
        else:
            return HttpResponse('frontpage')
            redirect('frontpage.html')
    else:
        form = RegistrationForm()
        arguments = {'form': form}
        return render(request, "register.html", arguments)

def gameregistration(request):
    if request.method == "POST":
        form = GameRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(home)
        else:
            return redirect(home)
    else:
        form = GameRegistrationForm()
        arguments = {'form':form}
        return render(request, "gameregistration.html", arguments)



def logout(request):
    logout(request)
