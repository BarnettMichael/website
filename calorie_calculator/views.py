from rest_framework import viewsets, permissions

from .models import Ingredient, Tag, Recipe, Instruction
from .serializers import IngredientSerializer, TagSerializer, RecipeSerializer, InstructionSerializer
from .permissions import IsUserAllowedToWrite

# Create your views here.


class IngredientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ingredients to be viewed or edited
    """

    queryset = Ingredient.objects.all().order_by('id')
    serializer_class = IngredientSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsUserAllowedToWrite)


class TagViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tags to be viewed or edited
    """

    queryset = Tag.objects.all().order_by('id')
    serializer_class = TagSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsUserAllowedToWrite)


class RecipeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Recipes to be viewed or edited
    """

    queryset = Recipe.objects.all().order_by('id')
    serializer_class = RecipeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsUserAllowedToWrite)


class InstructionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows instructions to be viewed or edited
    """

    queryset = Instruction.objects.all().order_by('id')
    serializer_class = InstructionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsUserAllowedToWrite)

