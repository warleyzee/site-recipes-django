from unicodedata import name
from django.shortcuts import render, get_list_or_404, get_object_or_404
from util.recipes.factory import make_recipe
from .models import Categoria,Receita

# Create your views here.s

def home(request):
    recipe = Receita.objects.filter(is_published=True).order_by('-id')
    return render(request, 'recipe/pages/home.html', context={
        'recipes' : recipe
    })

def Categoria(request, Categoria_id):
    recipes = get_list_or_404(
        Receita.objects.filter(
            Categoria__id=Categoria_id,
            is_published=True,
        ).order_by('-id')
    )

    return render(request, 'recipe/pages/category.html', context={
        'recipes': recipes,
        'title': f'{recipes[0].Categoria.name} - Category | '
    })

def recipe(request, id):
    recipe = Receita.objects.filter(
        pk=id,
        is_published = True,
    ).order_by('-id').first()
 
    return render(request, 'recipe/pages/recipe-view.html', context={
        'recipe' : recipe,
        'is_detail_page': True,
    })