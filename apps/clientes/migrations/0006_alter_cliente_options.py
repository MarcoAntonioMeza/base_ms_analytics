# Generated by Django 4.1 on 2024-12-25 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0005_alter_cliente_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'permissions': [('can_view_cliente', 'VER USUARIO'), ('can_update_cliente', 'ACTUALIZAR USUARIO'), ('can_create_cliente', 'CREAR USUARIO')]},
        ),
    ]