from django.db import models
from jsonfield import JSONField


class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    carbs = models.FloatField()
    sugar = models.FloatField()
    protein = models.FloatField()
    fat = models.FloatField()

    def __str__(self):
        return self.name


class Tag(models.Model):
    tag = models.CharField(max_length=20)

    def __str__(self):
        return self.tag


class Recipe(models.Model):

    name = models.CharField(max_length=200)
    ingredients = models.ManyToManyField(Ingredient)
    ingredients_dictionary = JSONField(null=True, blank=True)
    macros = models.CommaSeparatedIntegerField(max_length=10, blank=True)
    calories = models.PositiveIntegerField(default=0)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.name


class Instruction(models.Model):
    recipe = models.ForeignKey(Recipe)
    instruction = models.CharField(max_length=300)

    def __str__(self):
        return str(self.recipe) + ": " + str(self.instruction)
