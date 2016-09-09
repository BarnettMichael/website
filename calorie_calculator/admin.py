from django.contrib import admin

# Register your models here.
from .models import Ingredient, Tag, Recipe, Instruction

admin.site.register(Ingredient)
admin.site.register(Tag)
admin.site.register(Recipe)
admin.site.register(Instruction)


