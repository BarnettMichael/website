from django.contrib import admin
from .models import Post, Person, Guess, Match, Team

# Register your models here.

admin.site.register(Post)
admin.site.register(Person)
admin.site.register(Guess)
admin.site.register(Match)
admin.site.register(Team)