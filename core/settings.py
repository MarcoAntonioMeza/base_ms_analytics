import os
import dj_database_url
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
#CORE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


APPLY_LOAD_SEPOMEX = False


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2^_yk^ax2&0-aq%c(44f069a&@=%i$w2o6xn!^s-6%+b3h681w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
#DEBUG =True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '*']



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'whitenoise.runserver_nostatic'
    'widget_tweaks',
    'rest_framework',
    'apps.usuario',
    'apps.adminv2',
    'apps.clientes.apps.ClientesConfig',
    'direccion.apps.DireccionConfig',  # Registra la configuración de tu aplicación
    'apps.home',
    'apps.socialMedia',
    'apps.simulador',
    
    
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'
TEMPLATE_DIR = os.path.join(BASE_DIR, "apps/templates")  # ROOT dir for templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'components.NiftyComponent.listado_modulos',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

IS_LOCAL = False

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',  # Motor de base de datos
#        'NAME': 'base_django',  # Nombre de la base de datos
#        'USER': 'root',                 # Usuario de la base de datos
#        'PASSWORD': '',          # Contraseña del usuario
#        'HOST': '127.0.0.1',                  # Host (puede ser localhost o una IP)
#        'PORT': '3306',                       # Puerto de conexión, por defecto 3306
#        'OPTIONS': {
#            'sql_mode': 'STRICT_TRANS_TABLES',
#        },
#    }
#}

if not IS_LOCAL:
    DATABASES = {
        'default':  dj_database_url.config(default=os.getenv('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'base_project',       # Nombre de tu base de datos
            'USER': 'postgres',          # Usuario de la base de datos
            'PASSWORD': '2808',          # Contraseña del usuario
            'HOST': 'localhost',               # Dirección del servidor, 'localhost' para uso local
            'PORT': '5432',                    # Puerto de PostgreSQL (5432 es el predeterminado)
        }
    }

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization

LANGUAGE_CODE = 'es-Mx'

TIME_ZONE = 'America/Mexico_City'


USE_I18N = True
USE_L10N = True
USE_TZ = True



# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Lugar donde se recopilan los archivos estáticos
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'apps/static'),  # Carpetas donde se encuentran los archivos estáticos
]


# Directorio de archivos multimedia
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'usuario.Usuario'
LOGIN_URL = '/login'

CSRF_TRUSTED_ORIGINS = ['http://*','https://web-production-ce66.up.railway.app']