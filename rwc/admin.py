from django.contrib import admin
from .models import Post, Guess, Match, Team, User

# Register your models here.

admin.site.register(Post)
admin.site.register(Guess)
admin.site.register(Match)
admin.site.register(Team)
admin.site.register(User)