from django.forms import Select, ModelForm

from .models import Guess

class GuessForm(ModelForm):

    def __init__(self, *args, **kwargs):

        self.match = kwargs.pop('match')
        self.time = self.match.time
        super(GuessForm, self).__init__(*args, **kwargs)
        self.fields['winning_team'].widget.choices = [(self.match.home_team, self.match.home_team.name),
                                                      (self.match.away_team, self.match.away_team.name),
                                                     ]

    class Meta:
        model = Guess
        fields = ('winning_team', 'score_difference',)
        widgets = {'winning_team': Select()}