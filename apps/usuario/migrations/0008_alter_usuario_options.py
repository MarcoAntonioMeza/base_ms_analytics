# Generated by Django 4.1 on 2024-12-21 03:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0007_alter_usuario_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuario',
            options={'permissions': [('can_view', 'VER USUARIO'), ('can_update', 'ACTUALIZAR USUARIO')]},
        ),
    ]
