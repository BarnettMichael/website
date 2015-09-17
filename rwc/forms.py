from django import forms

from .models import Guess, Match

class GuessForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        self.match = kwargs.pop('match')
        super(GuessForm, self).__init__(*args, **kwargs)

        #Guess.objects.filter(user=self.user).filter(match=self.match)

    class Meta:
        model = Guess
        fields = ('match', 'winning_team', 'score_difference',)