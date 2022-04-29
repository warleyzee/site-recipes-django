from django.contrib import admin
from .models import Categoria, Receita, Tipos, Protudos
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

@admin.register(Protudos)
class ProtudosAdmin(admin.ModelAdmin):
    ...
