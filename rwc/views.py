import datetime

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import User, Team, Match, Guess
from .forms import GuessForm
# Create your views here.

def rwc_home(request):

    users = User.objects.all().order_by('points').reverse()
    print users
    upcoming_matches = Match.objects.all().order_by('time').exclude(time__lt=datetime.datetime.now())
    return render(request, 'rwc/rwc_home.html', {'upcoming_matches': upcoming_matches,
                                                 'users': users,
                                                 }
                  )


@login_required()
def rwc_guesses(request):

    user=request.user

    cut_off_time = datetime.datetime.now() - datetime.timedelta(minutes=5)

    print cut_off_time

    matches = Match.objects.all().order_by('time')
    guesses = Guess.objects.filter(user=user.user).exclude(match__time__lt=datetime.datetime.now())

    if request.method == "POST":

        match = request.POST['match']

        guess = Guess.objects.filter(user=user.user).filter(match=match)[0]
        form = GuessForm(request.POST, match=match, instance=guess)

        if form.is_valid():
            guess = form.save(commit=False)
            guess.user = user.user
            guess.save()

    forms = []
    for guess in guesses:

        form = GuessForm(instance=guess, match=guess.match)
        forms.append(form)
    print forms
    return render(request, 'rwc/rwc_guesses.html', {'user': user,
                                                    'forms': forms,
                                                    'matches': matches,
                                                    'guesses': guesses,
                                                    }
                    )