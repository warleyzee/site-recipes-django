from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('recipes/category/<int:category_id>/', views.category, name="recipes-category"),
    path('recipes/<int:id>/', views.recipe, name="recipes-recipe"),

] 