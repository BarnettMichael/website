from django.contrib import admin
from .models import Post, Guess, Match, Team, User

# Register your models here.

admin.site.register(Post)
admin.site.register(Guess)
admin.site.register(Team)


def update_scores(modeladmin, request, queryset):
    print queryset

def make_guesses(modeladmin, request, queryset):
    pass

class ScoreAdmin(admin.ModelAdmin):
    actions = [update_scores]

class MakeGuessesAdmin(admin.ModelAdmin):
    actions = [make_guesses]


admin.site.register(User, ScoreAdmin)
admin.site.register(Match, MakeGuessesAdmin)