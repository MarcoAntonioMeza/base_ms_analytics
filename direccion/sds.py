import pandas as pd
from django.db.models.signals import post_migrate
from django.dispatch import receiver
import time
from .models import Estado, Municipio, CodigoPostal, Colonia

@receiver(post_migrate)
def insertar_datos_iniciales(sender, **kwargs):
    # Iniciar el temporizador
    start_time = time.time()
    path = 'sepomex\CPdescarga.txt'
    df = pd.read_csv(path, delimiter="|", encoding="latin1")
    columnas_a_convertir = ['d_asenta','D_mnpio','d_estado']
    df[columnas_a_convertir] = df[columnas_a_convertir].apply(lambda x: x.str.strip().str.upper())
    print(df.shape)

    # Insertar Estados
    estados_a_insertar = []
    for _, row in df[['d_estado', 'c_estado']].drop_duplicates().iterrows():
        estado, created = Estado.objects.get_or_create(
            nombre=row['d_estado'],
            clave=row['c_estado']
        )
        if created:
            estados_a_insertar.append(estado)

    Estado.objects.bulk_create(estados_a_insertar)
    print(f"Tiempo de ejecución: {time.time() - start_time} segundos para estados")

    # Insertar Municipios
    municipios_a_insertar = []
    estados_dict = {estado.clave: estado for estado in Estado.objects.all()}  # Caché de estados

    for _, row in df[['D_mnpio', 'd_estado']].drop_duplicates().iterrows():
        estado = estados_dict.get(row['d_estado'])  # Obtener el estado del caché
        if estado:
            municipio, created = Municipio.objects.get_or_create(
                nombre=row['D_mnpio'],
                estado=estado
            )
            if created:
                municipios_a_insertar.append(municipio)

    Municipio.objects.bulk_create(municipios_a_insertar)
    print(f"Tiempo de ejecución: {time.time() - start_time} segundos para municipios")

    # Insertar Códigos Postales
    codigos_postales_a_insertar = []
    for _, row in df[['d_codigo', 'd_zona']].drop_duplicates().iterrows():
        codigo_postal, created = CodigoPostal.objects.get_or_create(
            codigo_postal=row['d_codigo'],
            defaults={'zona': row['d_zona']}  # Solo se inserta la zona si el registro es nuevo
        )
        if created:
            codigos_postales_a_insertar.append(codigo_postal)

    CodigoPostal.objects.bulk_create(codigos_postales_a_insertar)
    print(f"Tiempo de ejecución: {time.time() - start_time} segundos para códigos postales")

    # Insertar Colonias
    colonias_a_insertar = []
    municipios_dict = {municipio.nombre: municipio for municipio in Municipio.objects.all()}  # Caché de municipios
    codigos_postales_dict = {cp.codigo_postal: cp for cp in CodigoPostal.objects.all()}  # Caché de códigos postales

    for _, row in df[['d_asenta', 'd_tipo_asenta', 'd_codigo', 'D_mnpio']].drop_duplicates().iterrows():
        municipio = municipios_dict.get(row['D_mnpio'])  # Obtener municipio del caché
        if not municipio:
            # Si no existe el municipio, lo creamos
            estado = Estado.objects.get(nombre=row['d_estado'])
            municipio = Municipio.objects.create(
                nombre=row['D_mnpio'],
                estado=estado
            )
        
        codigo_postal = codigos_postales_dict.get(row['d_codigo'])  # Obtener código postal del caché
        if codigo_postal:
            colonia, created = Colonia.objects.get_or_create(
                d_asenta=row['d_asenta'],
                tipo_asentamiento=row['d_tipo_asenta'],
                municipio=municipio,
                codigo_postal=codigo_postal
            )
            if created:
                colonias_a_insertar.append(colonia)

    Colonia.objects.bulk_create(colonias_a_insertar)
    print(f"Tiempo de ejecución: {time.time() - start_time} segundos para colonias")

    end_time = time.time()
    elapsed_time = end_time - start_time

    # Convertir el tiempo en horas, minutos y segundos
    hours = int(elapsed_time // 3600)
    minutes = int((elapsed_time % 3600) // 60)
    seconds = int(elapsed_time % 60)

    # Imprimir el tiempo total
    print(f"Tiempo de ejecución total: {hours} horas, {minutes} minutos, {seconds} segundos")
    exit()