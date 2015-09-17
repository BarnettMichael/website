from django import forms

from .models import Guess

class GuessForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.match = kwargs.pop('match')
        super(GuessForm, self).__init__(*args, **kwargs)
        #self.fields['match'].widget.attrs['readonly'] = True


    class Meta:
        model = Guess
        fields = ('match', 'winning_team', 'points_difference',)