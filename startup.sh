#!/usr/bin/env bash
set -euo pipefail

if [ "${RUN_MIGRATIONS_ON_STARTUP:-0}" = "1" ]; then
  python manage.py migrate --noinput
fi

exec gunicorn --bind=0.0.0.0 --timeout 600 ProyectoSITU.wsgi:application --access-logfile - --error-logfile -
