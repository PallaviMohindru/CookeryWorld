from django.urls import path
import recipes.views


urlpatterns = [
    path('recipeslist/', recipes.views.recipeslist, name = 'recipeslist'),
    path('<int:recipes_id>',recipes.views.recipedetails, name = 'recipedetails' )

]
