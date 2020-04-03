from django.shortcuts import render, get_object_or_404
from .models import recipes

def recipeslist(request):
    myrecipes = recipes.objects
    return render(request,'recipes/recipeslist.html',{'rlist':myrecipes})

def recipedetails(request,recipes_id):
    recipe = get_object_or_404(recipes, pk = recipes_id)
    return render(request,'recipes/recipedetails.html', {'detail': recipe} )
