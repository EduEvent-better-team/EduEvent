# EduEvent

[Project overview and group responsibilities](Project Overview.md)

## Current scope

The project uses Django 5.2, PostgreSQL 17 and HTML templates. It includes the `core` module, URL routing, a shared `base.html` layout and a home page. The layout contains a header, a Home link, a content block and a footer. Backend code, frontend templates, database migrations and documentation have separate directories.

Event management, user-facing account screens, registration, attendance, reports, notifications and the calendar are not implemented yet.

## Local setup on Windows

Use Python 3.12 and Docker Desktop with Linux containers. Start Docker Desktop first. Run the following commands from the repository folder in PowerShell, one at a time:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
if (-not (Test-Path .env)) { Copy-Item .env.example .env }
# Set your local DB_PASSWORD in .env before starting the database.
docker compose up -d --wait db
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser. Stop the server with Ctrl+C.

The development setup uses PostgreSQL 17. Each contributor has their own database in Docker. Django reads connection settings from `.env`; only the `.env.example` template is shared. Keep your existing `.env`; the setup command only creates it when it is missing. Database data is stored in a persistent Docker volume. Stop the database with `docker compose stop db` and start it again with `docker compose up -d --wait db`. To start Django again, run the final `runserver` command above.

## Project structure

```text
eduevent/
  frontend/
    app/
      templates/base.html
      static/
    features/
      core/
        templates/core/home.html
        static/
  backend/
    app/                     # Django settings, main URLs, ASGI and WSGI
    modules/
      core/                  # Home page view and its URL configuration
    shared/                  # Small shared interfaces and error classes
  database/
    migrations/
      core/
    demo-data/
  docs/
  manage.py
  compose.yaml
  requirements.txt
  .env.example
```

`manage.py` is the command-line entry point in the project root. The `core` module is registered as `backend.modules.core.apps.CoreConfig`, with the Django app label `core`.

## Adding module pages

Each team develops its assigned Django app in `backend/modules/<module>/`. Set its `AppConfig.name` to `backend.modules.<module>`, register the app in `backend/app/settings.py`, and connect its URLs in `backend/app/urls.py`.

Put module templates in `frontend/features/<module>/templates/<module>/` and use `{% extends "base.html" %}`. Put module assets in `frontend/features/<module>/static/<module>/`. Restart Django after adding a new template or static directory so it reloads the directory list. Shared templates and assets belong in `frontend/app/`.

For each module, create the Python package `database/migrations/<module>/` with an `__init__.py` file, then add `<app_label>: "database.migrations.<module>"` to `MIGRATION_MODULES`. Run `makemigrations` and `migrate` through the root `manage.py`. Built-in Django migrations remain in the framework's installed packages.

Place initial JSON fixtures in `database/demo-data/`. Django can load them with `manage.py loaddata <filename>`. Keep requirements, UML diagrams and other documentation in `docs/`.

Agree on shared models and relationships before adding database fields. Keep application text and identifiers in English. Code comments may be in Polish.

## Development settings

This skeleton is configured for local development with `DEBUG=True`. `DJANGO_SECRET_KEY` can be supplied as an environment variable; the fallback is a public development-only value. Production deployment requires a private key and separate deployment configuration.
