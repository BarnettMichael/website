import datetime

from django.shortcuts import render
from django.contrib.auth.decorators import login_required


from .models import User, Team, Match, Guess
from .forms import GuessForm, GuessFormSet

# Create your views here.

def rwc_home(request):

    users = User.objects.all().order_by('points').reverse()

    matches_today = Match.objects.filter(time__year=datetime.datetime.today().year)\
                                 .filter(time__month=datetime.datetime.today().month)\
                                 .filter(time__day=datetime.datetime.today().day)\
                                 .order_by('time')

    matches_tomorrow = Match.objects.filter(time__year=datetime.datetime.today().year)\
                                    .filter(time__month=datetime.datetime.today().month)\
                                    .filter(time__day=(datetime.datetime.today().day + 1))\
                                    .order_by('time')

    return render(request, 'rwc/rwc_home.html', {'matches_today': matches_today,
                                                 'matches_tomorrow': matches_tomorrow,
                                                 'users': users,
                                                 }
                  )


@login_required()
def rwc_guesses(request):

    user=request.user

    pk=1

    matches = Match.objects.all().order_by('time')
    guesses = Guess.objects.filter(user=user.user)\
                    .exclude(match__time__lt=datetime.datetime.now())\
                    .exclude(match__time__gt=(datetime.datetime.now() + datetime.timedelta(days=7)))

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

    forms.reverse()

    print "GUESSES", guesses
    formset = GuessFormSet(queryset=guesses)
    for form in formset:
        print "Form", form.as_table()


    return render(request, 'rwc/rwc_guesses.html', {'user': user,
                                                    'forms': forms,
                                                    #'formset':formset,
                                                    'matches': matches,
                                                    'guesses': guesses,
                                                    'pk': pk,
                                                    }
                    )

def rwc_results(request):

    matches = Match.objects.filter(time__lt=datetime.datetime.now()).order_by('time')
    guesses = Guess.objects.filter(match__time__lt=datetime.datetime.now()).order_by('user')

    return render(request, 'rwc/rwc_results.html', {'matches': matches,
                                                    'guesses': guesses
                                                    }
                  )

@login_required()
def rwc_guesses_more(request, pk):

    user=request.user

    pk = int(pk)

    matches = Match.objects.all().order_by('time')
    guesses = Guess.objects.filter(user=user.user)\
                    .exclude(match__time__lt=(datetime.datetime.now() + (pk * datetime.timedelta(days=7))))\
                    .exclude(match__time__gt=(datetime.datetime.now() + ((pk + 1) * datetime.timedelta(days=7))))

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

    forms.reverse()

    return render(request, 'rwc/rwc_guesses.html', {'user': user,
                                                    'forms': forms,
                                                    'matches': matches,
                                                    'guesses': guesses,
                                                    'pk': pk + 1,
                                                    }
                  )