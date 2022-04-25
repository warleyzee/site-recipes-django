from unicodedata import name
from django.http import Http404
from django.shortcuts import render
from util.recipes.factory import make_recipe
from .models import Receita

# Create your views here.

def home(request):
    recipe = Receita.objects.filter(is_published = True).order_by('-id')
    return render(request, 'recipe/pages/home.html', context={
        'recipes' : recipe
    })

def category(request, category_id):
    recipe = Receita.objects.filter(category__id=category_id, is_published=True).order_by('-id')

    if not recipe:
        raise Http404('Not Found')


    return render(request, 'recipe/pages/category.html', context={
        'recipes' : recipe,
        'title': f'{recipe.first().category.name}  - Category | '
    })

def recipe(request, id):
    return render(request, 'recipe/pages/recipe-view.html', context={
        'recipe' : make_recipe(),
        'is_detail_page': True,
    })