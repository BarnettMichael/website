from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .models import Team, Match, Guess
from .forms import GuessForm
# Create your views here.

def rwc_home(request):

    matches = Match.objects.all().order_by('time')
    return render(request, 'rwc/rwc_home.html', {'matches': matches}
                  )


@login_required()
def rwc_guesses(request):

    user=request.user

    teams = Team.objects.all()
    matches = Match.objects.all()
    guesses = Guess.objects.all()


    if request.method == "POST":
        form = GuessForm(request.POST)
        if form.is_valid():
            guess = form.save(commit=False)
            guess.user = request.user._wrapped.user
            #guess.match = request.POST['match']
            guess.save()

    else:
        form = GuessForm()

    return render(request, 'rwc/rwc_guesses.html', {'user': user,
                                                    'form': form,
                                                    'matches': matches,
                                                    'guesses': guesses,
                                                    'teams': teams,
                                                    }
                    )