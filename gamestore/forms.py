from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Game, AllGames

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True)
    developer = forms.ChoiceField(required = False, choices={(1,'Yes'),(0,'No')})

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'developer'
        )

        def save(self, commit=True):
            user = super(RegistrationForm, self).save(commit=False)
            user.username = self.cleaned_data['username']
            user.email = self.cleaned_data['email']

            if commit:
                user.save()

            return user

class GameRegistrationForm(forms.ModelForm):
    class Meta:
        model = AllGames
        fields = ('game_name',
                'info',
                'game_url')
        def save(self, commit=True):
            game = super(GameRegistrationForm, self).save(commit=False)
            game.game_name = self.clened_data['game_name']
            game.info = self.cleaned_data['info']
            game.game_url = self.cleaned_data['game_url']

            if commit:
                game.save()

            return game
