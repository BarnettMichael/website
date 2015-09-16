from django import forms

from .models import Guess

class GuessForm(forms.ModelForm):

    class Meta:
        model = Guess
        fields = ('winning_team', 'points_difference')