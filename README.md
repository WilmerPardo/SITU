# SITU

Aplicacion Django del Sistema de Transporte Urbano SITU.

## Estructura

- `manage.py`: entrada principal de Django.
- `ProyectoSITU/`: configuracion del proyecto.
- `appSITUweb/`: modelos, vistas, formularios y administracion.
- `templates/`: plantillas HTML y archivos estaticos fuente.
- `requirements.txt`: dependencias necesarias para instalar en nube.
- `Procfile`: comando web para plataformas compatibles con buildpacks.

## Variables de entorno

Copia `.env.example` como referencia y configura estos valores en tu plataforma:

```env
DEBUG=False
SECRET_KEY=change-me
ALLOWED_HOSTS=tu-dominio.com
CSRF_TRUSTED_ORIGINS=https://tu-dominio.com
DATABASE_URL=
```

Si `DATABASE_URL` queda vacio, Django usa SQLite en `db.sqlite3`.

## Comandos utiles

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py runserver
```

Para ejecucion web en nube:

```bash
gunicorn ProyectoSITU.wsgi:application
```
