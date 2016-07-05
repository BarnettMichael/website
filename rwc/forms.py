from django.forms import Select, ModelForm, modelformset_factory

from .models import Guess

class GuessForm(ModelForm):

    def set_match_attributes(self, match):

        self.fields['winning_team'].widget.choices = [(match.home_team.id, match.home_team.name),
                                                     (match.away_team.id, match.away_team.name),
                                                     ]

        self.fields['match'].widget.choices = [(match.id, match)]



    class Meta:
        model = Guess
        fields = ('match', 'winning_team', 'score_difference',)
        widgets = {'winning_team': Select(),
                   'match': Select(),
                   }

GuessFormSet = modelformset_factory(Guess,
                                    form=GuessForm,
                                    extra=0
                                    )