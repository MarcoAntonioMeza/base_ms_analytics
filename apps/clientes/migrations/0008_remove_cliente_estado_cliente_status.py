# Generated by Django 4.1 on 2024-12-25 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0007_alter_cliente_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='estado',
        ),
        migrations.AddField(
            model_name='cliente',
            name='status',
            field=models.IntegerField(choices=[(10, 'ACTIVO'), (20, 'INACTIVO')], default=10, verbose_name='Status'),
        ),
    ]
