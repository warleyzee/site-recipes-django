from django.contrib import admin
from .models import Category, Recipes
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    ...

@admin.register(Recipes)
class ReceitaAdmin(admin.ModelAdmin):
    ...

admin.site.register(Category, CategoryAdmin)