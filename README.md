# Djcds

una aplicacion web simple hecha para administrar una galeria de cds, en verdad la tematica podria ser diferente
solo controla modelos de una base de datos con relaciones ForeingKey para otros modelos.

## Tecnologias

1. Django (BackEnd)
2. Bootstrap (FrontEnd)
3. PostreSQL (Database)
4. Ajax (Vanilla Javascript)

## instalacion

en el caso que quieras replicar el sitio seria instalar el interprete de python y luego el paquete de django junto a psycopg2-

```python-console
pip install django
pip install psycopg2
```

junto a postgresql, de ahi si sabes ocupar django sabes lo que tienes que hacer para configurar base de datos, añadir vistas, urls, templates, archivos estaticos, añadir apps, modelos etc.

### info extra

varios archivos considerados inutilizables en el repositorio de GitHub no estan incluidos, como los archivos "pycache" de el proyecto y los archivos migrations de las apps.

tambien esta ignorado el archivo settings.py y manage.py, uno porque tiene datos privados como el "SECRET_KEY" y algunas otras cosas, entre ellas los datos usados para el correo de la recuperacion de contraseñas, aqui van unos datos de cosas importantes del archivo settings.py que no pudieron ser mostradas por las razones anteriores.

```python
import os
from django.urls import reverse_lazy
```

headers extra

```python
DATABASES = {
    "default": {
        "ENGINE": "{el relacionado a tu base de datos}",
        "NAME": "{nombre de la base de datos}",
        "USER": "{nombre del usuario de la base de datos}",
        "PASSWORD": "{contraseñas del usuario}",
        "HOST": "{host}",
        "PORT": "{puerto}",
    }
}
```

añadir base de datos
remplazando cada valor por su equivalente

```python
INSTALLED_APPS = [
    "album",
    "maintenance",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

```

añadir las apps

```python
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
```

las templates

```python
STATIC_URL = "/static/"
STATIC_ROOT = "staticfiles"
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
```

archivos estaticos

```python
LOGIN_REDIRECT_URL = reverse_lazy("album:album_list")
LOGOUT_REDIRECT_URL = reverse_lazy("login")
```

y los redirects despues de un logeo y deslogeo
