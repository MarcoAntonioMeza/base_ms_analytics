# Generated by Django 4.1 on 2024-12-18 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulador', '0003_alter_solicitud_created_at_alter_solicitud_pago'),
    ]

    operations = [
        migrations.CreateModel(
            name='SimuladorSolicitudView',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('consumo_kwh', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pago', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cantidad_energia_ahorrada', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cliente_id', models.IntegerField()),
                ('estado_id', models.IntegerField()),
                ('estado', models.CharField(max_length=255)),
                ('nombres', models.CharField(max_length=255)),
                ('fecha', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Simulador Solicitud',
                'verbose_name_plural': 'Simulador Solicitudes',
                'db_table': 'simulador_solicitud_view',
                'managed': False,
            },
        ),
    ]
