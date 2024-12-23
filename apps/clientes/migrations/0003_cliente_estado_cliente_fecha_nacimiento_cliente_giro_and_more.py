# Generated by Django 4.1 on 2024-12-22 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('direccion', '0002_alter_estado_options'),
        ('clientes', '0002_alter_cliente_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='estado',
            field=models.IntegerField(choices=[(10, 'ACTIVO'), (20, 'INACTIVO')], default=10, verbose_name='Estado'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='fecha_nacimiento',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='Fecha de nacimiento'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='giro',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Giro'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='telefono2',
            field=models.CharField(blank=True, default=None, max_length=10, null=True, verbose_name='Teléfono celular 2'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.CharField(max_length=10, verbose_name='Teléfono celular'),
        ),
        migrations.CreateModel(
            name='DireccionClientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calle', models.CharField(max_length=200)),
                ('numero_exterior', models.CharField(blank=True, max_length=20, null=True)),
                ('numero_interior', models.CharField(blank=True, max_length=20, null=True)),
                ('codigo_postal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='direccion.codigopostal')),
                ('colonia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='direccion.colonia')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='direccion.estado')),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='direccion.municipio')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='direcciones', to='clientes.cliente')),
            ],
        ),
    ]