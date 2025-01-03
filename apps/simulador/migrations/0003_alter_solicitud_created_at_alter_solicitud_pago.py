# Generated by Django 4.1 on 2024-12-15 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulador', '0002_alter_solicitud_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación'),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='pago',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Pago'),
        ),
    ]
