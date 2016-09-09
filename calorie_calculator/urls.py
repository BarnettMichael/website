from django.conf.urls import url, include
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r'ingredients', views.IngredientViewSet)
router.register(r'tags', views.TagViewSet)
router.register(r'recipes', views.RecipeViewSet)
router.register(r'instructions', views.InstructionViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    ]
