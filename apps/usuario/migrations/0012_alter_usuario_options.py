# Generated by Django 4.1 on 2025-01-05 03:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0011_alter_usuario_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuario',
            options={'permissions': [('can_view_user', 'VER USUARIO'), ('can_update_user', 'ACTUALIZAR USUARIO'), ('can_create_user', 'CREAR USUARIO'), ('can_delete_user', 'ELIMINAR USUARIO')]},
        ),
    ]
