# Generated by Django 4.1 on 2025-01-02 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialMedia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='count_likes',
            field=models.IntegerField(default=0, verbose_name='Número de Me Gusta'),
        ),
    ]