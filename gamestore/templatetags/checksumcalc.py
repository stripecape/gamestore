from django import template
from hashlib import md5
from gamestore.models import Store, AllGames

register = template.Library()

def calculateChecksum(pid):
    game = AllGames.objects.get(id=pid)
    store = Store.objects.get(id=1)

    sid = store.sid
    amount = game.price
    secret_key = store.key

    checksumstr = "pid={}&sid={}&amount={}&token={}".format(pid, sid, amount, secret_key)
    return m.hexdigest()
