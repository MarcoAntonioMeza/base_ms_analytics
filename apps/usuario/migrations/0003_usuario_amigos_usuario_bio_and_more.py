# Generated by Django 4.1 on 2024-12-12 04:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_usuario_created_at_usuario_created_by_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='amigos',
            field=models.ManyToManyField(blank=True, related_name='amigos_conectados', to=settings.AUTH_USER_MODEL, verbose_name='Amigos'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='bio',
            field=models.TextField(blank=True, null=True, verbose_name='Biografía'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='name_soacial_media',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Nombre de la red social'),
        ),
    ]
