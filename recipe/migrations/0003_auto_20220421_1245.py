# Generated by Django 3.2.6 on 2022-04-21 11:45

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipe', '0002_auto_20220421_1232'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Recipes',
            new_name='Receita',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='author',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='category',
        ),
    ]