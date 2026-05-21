# SITU

Aplicacion Django del Sistema de Transporte Urbano SITU.

## Estructura

- `manage.py`: entrada principal de Django.
- `ProyectoSITU/`: configuracion del proyecto.
- `appSITUweb/`: modelos, vistas, formularios y administracion.
- `templates/`: plantillas HTML y archivos estaticos fuente.
- `requirements.txt`: dependencias necesarias para instalar en nube.
- `Procfile`: comando web para plataformas compatibles con buildpacks.
- `startup.sh`: comando de arranque recomendado para Azure App Service.
- `docs/azure-deploy.md`: guia de despliegue en Azure.

## Variables de entorno

Copia `.env.example` como referencia y configura estos valores en tu plataforma:

```env
DEBUG=False
SECRET_KEY=change-me
ALLOWED_HOSTS=tu-dominio.com
CSRF_TRUSTED_ORIGINS=https://tu-dominio.com
DATABASE_URL=postgresql://usuario:password@servidor.postgres.database.azure.com:5432/situ
DB_SSL_MODE=require
SECURE_SSL_REDIRECT=True
SECURE_HSTS_SECONDS=0
```

Si `DATABASE_URL` queda vacio, Django usa SQLite en `db.sqlite3`.
En Azure tambien se puede conectar PostgreSQL con las variables `AZURE_POSTGRESQL_NAME`, `AZURE_POSTGRESQL_USER`, `AZURE_POSTGRESQL_PASSWORD` y `AZURE_POSTGRESQL_HOST`.

Para imagenes subidas en produccion, configura Azure Blob Storage con:

```env
AZURE_STORAGE_CONNECTION_STRING=DefaultEndpointsProtocol=...
AZURE_STORAGE_CONTAINER=media
```

## Comandos utiles

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py runserver
```

Para ejecucion web en nube:

```bash
gunicorn --bind=0.0.0.0 --timeout 600 ProyectoSITU.wsgi:application --access-logfile - --error-logfile -
```

## Azure App Service

La guia completa esta en [`docs/azure-deploy.md`](docs/azure-deploy.md).

Resumen:

1. Crear un App Service Linux con runtime Python 3.13.
2. Configurar PostgreSQL y las variables de entorno en **Settings > Environment variables**.
3. Configurar el startup command en **Settings > Configuration > General settings**:

```bash
bash startup.sh
```

4. Conectar GitHub desde **Deployment > Deployment Center** apuntando a `WilmerPardo/SITU`, branch `main`.
5. Ejecutar migraciones desde **Development Tools > SSH**:

```bash
python manage.py migrate --noinput
```
