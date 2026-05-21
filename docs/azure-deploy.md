# Despliegue de SITU en Azure App Service

Esta aplicacion esta preparada para ejecutarse en Azure App Service para Linux con Django, Gunicorn, WhiteNoise, PostgreSQL o MySQL, y almacenamiento opcional de imagenes en Azure Blob Storage.

## Recursos recomendados

- App Service para Linux con runtime Python 3.13.
- Azure Database for PostgreSQL Flexible Server para la base de datos. Si tu suscripcion no ofrece PostgreSQL, usa Azure Database for MySQL Flexible Server.
- Storage Account con un contenedor `media` si vas a conservar imagenes subidas.
- GitHub como origen de despliegue continuo.

## Configuracion en Azure Portal

1. Entra a https://portal.azure.com.
2. Ve a **App Services** > **Create** > **Web App**.
3. En **Basics**:
   - **Publish**: Code.
   - **Runtime stack**: Python 3.13.
   - **Operating System**: Linux.
   - Crea o selecciona un **App Service Plan**.
4. En **Deployment** puedes activar GitHub Actions o dejarlo para configurar despues desde **Deployment Center**.
5. Crea la aplicacion.

## Variables de entorno

En tu Web App entra a **Settings** > **Environment variables** > **App settings** y configura:

```env
DEBUG=False
SECRET_KEY=un-valor-largo-y-secreto
SCM_DO_BUILD_DURING_DEPLOYMENT=1
DATABASE_URL=postgresql://usuario:password@servidor.postgres.database.azure.com:5432/situ
DB_SSL_MODE=require
SECURE_SSL_REDIRECT=True
SECURE_HSTS_SECONDS=0
```

Si usas Azure Database for MySQL Flexible Server, usa este formato:

```env
DATABASE_URL=mysql://usuario:password@servidor.mysql.database.azure.com:3306/situ
DB_SSL_MODE=require
```

`ALLOWED_HOSTS` y `CSRF_TRUSTED_ORIGINS` pueden configurarse manualmente, pero la app tambien agrega automaticamente el hostname que Azure expone en `WEBSITE_HOSTNAME`.

Si usas Blob Storage para imagenes, agrega:

```env
AZURE_STORAGE_CONNECTION_STRING=DefaultEndpointsProtocol=...
AZURE_STORAGE_CONTAINER=media
AZURE_STORAGE_URL_EXPIRATION_SECS=3600
```

Si no usas Blob Storage, agrega:

```env
DJANGO_MEDIA_ROOT=/home/site/media
```

Cuando ya tengas dominio y certificado estables, puedes subir `SECURE_HSTS_SECONDS` a `31536000`.

## Startup Command

En **Settings** > **Configuration** > **General settings**, usa este startup command:

```bash
bash startup.sh
```

Para ejecutar migraciones automaticamente en cada arranque, configura `RUN_MIGRATIONS_ON_STARTUP=1`. Para produccion con mas de una instancia, es mas seguro dejarlo en `0` y ejecutar migraciones manualmente.

## Despliegue continuo desde GitHub

1. En la Web App entra a **Deployment** > **Deployment Center**.
2. En **Source**, selecciona **GitHub**.
3. Autoriza tu cuenta si Azure lo solicita.
4. Selecciona:
   - Organization: `WilmerPardo`
   - Repository: `SITU`
   - Branch: `main`
5. Guarda la configuracion.

Azure generara o usara un flujo de despliegue. Cada commit enviado a `main` desplegara la app.

## Migraciones

Despues del primer despliegue:

1. En la Web App entra a **Development Tools** > **SSH**.
2. Pulsa **Go**.
3. Ejecuta:

```bash
python manage.py migrate --noinput
python manage.py createsuperuser
```

## Logs

- Logs de build: **Deployment** > **Deployment Center** > **Logs**.
- Logs de ejecucion: **Monitoring** > **Log stream**.

Referencias oficiales:

- https://learn.microsoft.com/en-us/azure/app-service/configure-language-python
- https://learn.microsoft.com/en-us/azure/app-service/tutorial-python-postgresql-app-django
- https://learn.microsoft.com/en-us/azure/app-service/deploy-continuous-deployment
