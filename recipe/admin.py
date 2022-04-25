from django.contrib import admin
from .models import Category, Recipe, Receita
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    ...

# @admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
    ...

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):

    ...

admin.site.register(Category, CategoryAdmin)
admin.site.register(Receita, ReceitaAdmin)
