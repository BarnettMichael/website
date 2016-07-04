from django.forms import Select, ModelForm, modelformset_factory

from .models import Guess

class GuessForm(ModelForm):

    def __init__(self, *args, **kwargs):

        self.match = kwargs.pop('match')

        self.time = self.match.time

        super(GuessForm, self).__init__(*args, **kwargs)

        self.fields['winning_team'].widget.choices = [(self.match.home_team.id, self.match.home_team.name),
                                                      (self.match.away_team.id, self.match.away_team.name),
                                                      ]

        self.fields['match'].widget.choices = [(self.match.id, self.match)]


    class Meta:
        model = Guess
        fields = ('match', 'winning_team', 'score_difference',)
        widgets = {'winning_team': Select(),
                   'match': Select(),
                   }

GuessFormSet = modelformset_factory(Guess, fields=('match', 'winning_team', 'score_difference'),
                                widgets={
                                    'winning_team': Select(),
                                    'match': Select(),
                                }, extra=0
                                    )