from models import Ingredient, Tag, Recipe, Instruction
from rest_framework import serializers


class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'carbs', 'sugar', 'protein', 'fat')


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'tag')


class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Recipe
        fields = ('id', 'name', 'ingredients', 'macros', 'calories',
                  'tags', 'ingredients_dictionary')

    # http://www.django-rest-framework.org/api-guide/relations/#writable-nested-serializers
    # def create(self, validated_data):
    #     ingredients_data = validated_data.pop('ingredients')
    #
    #     recipe = Recipe.objects.create(**validated_data)
    #     for ingredient in ingredients_data:
    #         Ingredient.objects.create(recipe=recipe, **ingredient)
    #
    #     return recipe
    #
    # def update(self, validated_data):
    #     ingredients_data = validated_data.pop('ingredients')
    #
    #     recipe = Recipe.Objects.get(id=validated_data.pop('id'))


class InstructionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Instruction
        fields = ('id', 'recipe', 'instruction')
