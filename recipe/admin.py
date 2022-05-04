from django.contrib import admin
<<<<<<< HEAD
from .models import Categoria, Receita, Tipos, Protudos
=======
from .models import Category, Recipes
>>>>>>> a8214af32b3fe13b82ad089af855517754f2be2d
# Register your models here.

# @admin.register(Categoria)
# class CategoriaAdmin(admin.ModelAdmin):
#     ...


# @admin.register(Receita)
# class ReceitasAdmin(admin.ModelAdmin):
#    ...

@admin.register(Tipos)
class TiposAdmin(admin.ModelAdmin):
    ...

<<<<<<< HEAD
@admin.register(Protudos)
class ProtudosAdmin(admin.ModelAdmin):
=======
@admin.register(Recipes)
class ReceitaAdmin(admin.ModelAdmin):
>>>>>>> a8214af32b3fe13b82ad089af855517754f2be2d
    ...
