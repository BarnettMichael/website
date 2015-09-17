from django.contrib import admin
import datetime

from .models import Post, Guess, Match, Team, User

# Register your models here.

admin.site.register(Post)
admin.site.register(Guess)
admin.site.register(Team)


def update_scores(modeladmin, request, queryset):
    for user in queryset:
        print user, user.points
        user.points = 0
        print user, user.points
        guess_query = Guess.objects.filter(user=user)\
                            .exclude(match__time__gt=datetime.datetime.now())
        for guess in guess_query:
            print "MATCH:" , guess.match
            if guess.match.score_difference != 0:
                if guess.winning_team == guess.match.winning_team:
                    user.points += 3
                    if guess.score_difference == guess.match.score_difference:
                        user.points += 2
            else:
                if guess.score_difference == guess.match.score_difference:
                    user.points += 5

        print user, user.points
        user.save()


def make_guesses(modeladmin, request, queryset):
    for match in queryset:
        for user in User.objects.all():
            Guess.objects.create(
                match=match,
                user=user,
            )

class ScoreAdmin(admin.ModelAdmin):
    actions = [update_scores]

class MakeGuessesAdmin(admin.ModelAdmin):
    actions = [make_guesses]


admin.site.register(User, ScoreAdmin)
admin.site.register(Match, MakeGuessesAdmin)