from django.db import models
import uuid

# Create your models here.
class Ingredient(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    carbs = models.IntegerField()
    sugar = models.IntegerField()
    protein = models.IntegerField()
    fat = models.IntegerField()

    def __str__(self):
        return self.name


class Recipe(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    ingredients = {}
    macros = {}
    calories = models.PositiveIntegerField()
    instructions = []
    tags = []

    def __str__(self):
        return self.name