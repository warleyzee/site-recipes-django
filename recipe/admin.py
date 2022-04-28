from django.contrib import admin
<<<<<<< HEAD
from .models import Category, Recipes
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    ...

@admin.register(Recipes)
class ReceitaAdmin(admin.ModelAdmin):
    ...

admin.site.register(Category, CategoryAdmin)
=======

# Register your models here.
>>>>>>> c0f2431b99c704a27262d6a5d7e81d675cbb0e24
