from rest_framework import viewsets

from .models import Ingredient, Recipe
from .serializers import IngredientSerializer, RecipeSerializer

# Create your views here.

class IngredientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ingredients to be viewed or edited
    """

    queryset = Ingredient.objects.all().order_by('id')
    serializer_class = IngredientSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Recipes to be viewed or edited
    """

    queryset = Recipe.objects.all().order_by('id')
    serializer_class = RecipeSerializer