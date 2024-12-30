from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render


def listado_modulos(request):
    modulos = [
        {
            'nombre': 'CONFIGURACION',
            'url': 'user_index',
            'app': 'usuario',
            'icono': 'fa-cogs',  # Icono para el módulo 'USUARIOS'
            'submodulos': [
                {
                    'app': 'usuario',
                    'nombre': 'Usuarios',
                    'permiso': 'can_view_user',
                    'url': 'user_index',
                    'icono': 'fa-eye',  # Icono para el submódulo 'Ver Usuarios'
                },
                {
                    'app': 'auth',
                    'nombre': 'Grupos',
                    'permiso': 'can_view_grupo',
                    'url': 'grupos_index',
                    'icono': 'fa-eye',  # Icono para el submódulo 'Ver Usuarios'
                },
                # Más submódulos pueden añadirse aquí
            ]
        },
        {
            'nombre': 'CLIENTES',
            'url': 'can_view_cliente',
            'app': 'clientes',
            'icono': 'fa-store',  # Icono para el módulo 'Ventas'
            'submodulos': [
                {
                    'app': 'clientes',
                    'nombre': 'Clientes',
                    'permiso': 'can_view_cliente',
                    'url': 'clientes_index',#clientes_index
                    'icono': 'fa-search',  # Icono para el submódulo 'Ver Ventas'
                },
               
            ]
        },
        # Otros módulos...
    ]
    
    if request.user.is_authenticated:
        #print( request.user.get_all_permissions(),'permisos')
        permisos_usuario = request.user.get_all_permissions()
        #print(permisos_usuario,'permisos')
        modulos_accesibles = []

        for modulo in modulos:
            modulos_acc = {
                'nombre': modulo['nombre'],
                'url': modulo['url'],
                'icono': modulo['icono'],  # Incluir el ícono del módulo
                'submodulos': [],
            }
            for submodulo in modulo['submodulos']:
                if f'{submodulo["app"]}.{submodulo["permiso"]}' in permisos_usuario:
                    modulos_acc['submodulos'].append(submodulo)
            
            if modulos_acc['submodulos']:
                modulos_accesibles.append(modulos_acc)
                
        
        #print(modulos_accesibles, 'hay usuarios')
        return {'modulos_accesibles': modulos_accesibles}
        #print(modulos_accesibles,'no hay usuarisdsd')    
    return {'modulos_accesibles': []}
