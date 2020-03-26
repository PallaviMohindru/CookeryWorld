from django.shortcuts import render

def recipeslist(request):
    return render(request,'recipes/recipeslist.html')
