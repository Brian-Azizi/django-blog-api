# Generated by Django 2.0 on 2018-01-06 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_comment'),
        ('profiles', '0002_profile_follows'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='favorites',
            field=models.ManyToManyField(related_name='favorited_by', to='articles.Article'),
        ),
    ]
