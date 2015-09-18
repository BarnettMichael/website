import datetime

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import User, Team, Match, Guess
from .forms import GuessForm

# Create your views here.

def rwc_home(request):

    users = User.objects.all().order_by('points').reverse()
    upcoming_matches = Match.objects.all().order_by('time').exclude(time__lt=datetime.datetime.now())
    matches_today = Match.objects.filter(time__year=datetime.datetime.today().year)\
                                 .filter(time__month=datetime.datetime.today().month)\
                                 .filter(time__day=datetime.datetime.today().day)

    matches_tomorrow = Match.objects.filter(time__year=datetime.datetime.today().year)\
                                    .filter(time__month=datetime.datetime.today().month)\
                                    .filter(time__day=(datetime.datetime.today().day + 1))

    return render(request, 'rwc/rwc_home.html', {'upcoming_matches': upcoming_matches,
                                                 'matches_today': matches_today,
                                                 'matches_tomorrow': matches_tomorrow,
                                                 'users': users,
                                                 }
                  )


@login_required()
def rwc_guesses(request):

    user=request.user

    matches = Match.objects.all().order_by('time')
    guesses = Guess.objects.filter(user=user.user)\
                    .exclude(match__time__lt=datetime.datetime.now())\
                    .exclude(match__time__gt=(datetime.datetime.now() + datetime.timedelta(days=4)))

    if request.method == "POST":

        match = Match.objects.get(pk=(request.POST['match']))
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
    return render(request, 'rwc/rwc_guesses.html', {'user': user,
                                                    'forms': forms,
                                                    'matches': matches,
                                                    'guesses': guesses,
                                                    }
                    )