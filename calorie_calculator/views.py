from rest_framework import viewsets

from .models import Ingredient, Tag, Recipe, Instruction
from .serializers import IngredientSerializer, TagSerializer, RecipeSerializer, InstructionSerializer

# Create your views here.


class IngredientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ingredients to be viewed or edited
    """

    queryset = Ingredient.objects.all().order_by('id')
    serializer_class = TagSerializer


class TagViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tags to be viewed or edited
    """

    queryset = Tag.objects.all().order_by('id')
    serializer_class = IngredientSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Recipes to be viewed or edited
    """

    queryset = Recipe.objects.all().order_by('id')
    serializer_class = RecipeSerializer


class InstructionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows instructions to be viewed or edited
    """

    queryset = Instruction.objects.all().order_by('id')
    serializer_class = InstructionSerializer
