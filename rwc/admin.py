from django.contrib import admin
import datetime

from .models import Post, Guess, Match, Team, User

# Register your models here.

admin.site.register(Post)
admin.site.register(Guess)
admin.site.register(Team)


# def update_scores(modeladmin, request, queryset):
#     for user in queryset:
#         print user, user.points
#         user.points = 0
#         print user, user.points
#         guess_query = Guess.objects.filter(user=user)\
#                             .exclude(match__time__gt=datetime.datetime.now())
#         for guess in guess_query:
#             print "MATCH:" , guess.match
#             if guess.match.score_difference != 0:
#                 if guess.winning_team == guess.match.winning_team:
#                     user.points += 3
#                     if guess.score_difference == guess.match.score_difference:
#                         user.points += 2
#             else:
#                 if guess.score_difference == guess.match.score_difference:
#                     user.points += 5
#
#         print user, user.points
#         user.save()

def update_scores(modeladmin, request, queryset):
    """
    Independent of parameters
    resets all users scores to 0
    iterates through each match that has already occurred and sets points accordingly
    collects a list of difference between guessed scores and actual score
    gives bonus point to user(s) who are closest.
    """

    matches = Match.objects.filter(time__lt=datetime.datetime.now())
    users = User.objects.all()

    for user in users:
        user.points = 0
        user.save()

    for match in matches:
        point_differences = []
        match_guesses = Guess.objects.filter(match=match)
        for guess in match_guesses:
            user = guess.user
            if match.score_difference != 0:
                if guess.winning_team == match.winning_team:
                    user.points += 3
                    point_differences.append(abs(guess.score_difference - guess.match.score_difference))

                    if guess.score_difference == match.score_difference:
                        user.points += 1
            else:
                if guess.score_difference == match.score_difference:
                    user.points += 4

            user.save()

        # Check if anybody guessed guessed the correct winning team, and if so give bonus point to user
        # who is closest.

        if bool(point_differences):                                       # empty_list == False
            for guess in match_guesses:
                user = guess.user
                if guess.winning_team == match.winning_team:
                    if abs(guess.score_difference - match.score_difference) == min(point_differences):
                        user.points += 1
                        user.save()

def make_guesses(modeladmin, request, queryset):
    """
    Populates each match in the queryset with a default guess for each user.
    """
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