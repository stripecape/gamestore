from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class StoreUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #name = models.CharField(max_length = 150, unique = True, null=True)
    #user_email = models.EmailField(blank = True, null=True)
    #user_password = models.CharField(max_length = 30, null=True)
    developer = models.IntegerField(default=0)
    money = models.PositiveIntegerField(default=100)

    #class Meta:
        #managed = True


    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        StoreUser.objects.create(user=instance)
    instance.storeuser.save()

    """def set_as_developer(self):
        self.developer = True;
        self.save()

    def get_is_developer(self):
        return self.developer"""

"""@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        StoreUser.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.storeuser.save()"""

#Luo profiilin
"""def create_profile(sender, **kwargs):
    #Jos käyttäjäobjekti on luotu, niin profiili luodaan.
    if kwargs['created']:
        user_profile = StoreUser.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)"""

class Game(models.Model):
    game_name = models.CharField(max_length = 150, blank = True, null=True)
    game_url = models.URLField(null=True)
    game_info = models.TextField(blank = True, null = True)
    high_score = models.IntegerField(default = 0, null=True)
    player = models.ForeignKey("StoreUser", on_delete = models.CASCADE, null = True, related_name = "game" )

class AllGames(models.Model):
    game_name = models.CharField(max_length = 150, blank = True, null=True)
    game_url = models.URLField(null=True)
    info = models.TextField(blank=True)
    high_score = models.IntegerField(default = 0, null=True)
    developer_id = models.ForeignKey("StoreUser", on_delete = models.CASCADE, null = True, related_name = "game_in_store")
    sold = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.game_name

    #def add_new_game(self):
    #def remove_game(self):

class Sales(models.Model):
    date = models.DateField(auto_now_add=True)
    sold_game = models.ForeignKey("AllGames", on_delete = models.CASCADE, null = True, related_name = "sales_info")

class Store(models.Model):
    id = models.AutoField(primary_key=True)
    pid = models.PositiveIntegerField(default =0, blank = False, null = False)
    sid = models.CharField(max_length = 20, blank = False, null = False, default="xdxachepeedzsnhs")
    key = models.CharField(max_length = 50, blank = False, null = False, default="22bb869888dc66715cf61785277bfad3")
    amount = models.PositiveIntegerField(default =0, blank = False, null = False)
    checksum = models.CharField(max_length = 100, blank = False, null = False, default="")
