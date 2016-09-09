from models import Ingredient, Tag, Recipe, Instruction
from rest_framework import serializers


class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('name', 'carbs', 'sugar', 'protein', 'fat')


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = 'tag'


class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recipe
        fields = ('name', 'ingredients', 'macros', 'calories', 'tags', 'ingredients_dictionary')


class InstructionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Instruction
        fields = ('recipe', 'instruction')
