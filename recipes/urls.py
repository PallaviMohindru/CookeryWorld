from django.urls import path
import recipes.views


urlpatterns = [
    path('recipeslist/', recipes.views.recipeslist, name = 'recipeslist'),

]
