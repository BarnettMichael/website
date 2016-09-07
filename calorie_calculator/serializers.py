from models import Ingredient, Recipe
from rest_framework import  serializers

class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'carbs', 'sugar', 'protein', 'fat')


class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recipe
        fields = ('id', 'name', 'ingredients', 'macros', 'calories', 'instructions', 'tags')