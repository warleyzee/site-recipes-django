from django.db import models
from django.contrib.auth.models import User

# Create your models here.

  
class Tipos(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name

<<<<<<< HEAD
class Protudos(models.Model):
    title = models.CharField(max_length=70)
    description = models.CharField(max_length=70)
    slug = models.SlugField()
    preparation_time = models.CharField(max_length=70)
    preparation_time_unit = models.CharField(max_length=70)
    servings = models.CharField(max_length=70)
    servings_unit = models.CharField(max_length=70)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/')
    category = models.ForeignKey(Tipos, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

class Categoria(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name

class Receita(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
=======
class Recipes(models.Model):
    title = models.CharField(max_length=70)
    description = models.CharField(max_length=170)
>>>>>>> a8214af32b3fe13b82ad089af855517754f2be2d
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=70)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=70)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/')
    category = models.ForeignKey(
        Categoria, on_delete=models.SET_NULL, null=True
    )
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )


    def __str__(self):
        return self.title 
<<<<<<< HEAD
  
=======
>>>>>>> a8214af32b3fe13b82ad089af855517754f2be2d
