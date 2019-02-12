from django.contrib import admin
from gamestore.models import StoreUser, Game, AllGames, Sales, Store

# Register your models here.
admin.site.register(StoreUser)
admin.site.register(Game)
admin.site.register(AllGames)
admin.site.register(Sales)
admin.site.register(Store)
