# Generated by Django 4.1 on 2024-12-11 03:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CodigoPostal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_postal', models.CharField(max_length=10, unique=True)),
                ('zona', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('clave', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='direccion.estado')),
            ],
        ),
        migrations.CreateModel(
            name='Colonia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_asenta', models.CharField(max_length=100)),
                ('tipo_asentamiento', models.CharField(max_length=50)),
                ('codigo_postal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='direccion.codigopostal')),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='direccion.municipio')),
            ],
        ),
    ]
