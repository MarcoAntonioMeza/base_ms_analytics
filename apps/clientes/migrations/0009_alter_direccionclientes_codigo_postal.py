# Generated by Django 5.1.4 on 2025-01-06 02:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0008_remove_cliente_estado_cliente_status'),
        ('direccion', '0002_alter_estado_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direccionclientes',
            name='codigo_postal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='direccion.codigopostal'),
        ),
    ]
