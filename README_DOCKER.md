# Docker deployment (development / simple production)

This repository includes a `Dockerfile` and `docker-compose.yml` to run the WineshopDemo1 app with PostgreSQL.

Quick start (development):

1. Copy the example env file and edit:

```bash
cp .env.example .env
# edit .env and set SECRET_KEY and POSTGRES_PASSWORD
```

2. Build and start with docker-compose:

```bash
docker-compose up --build
```

The Flask app will be available at `http://localhost:8000`.

Notes for production:
- For a public deployment use an external reverse proxy (NGINX) for TLS termination and serving static files.
- Use a managed database or separate Postgres container with persistent volumes and backups.
- Do NOT commit `.env` to source control — keep secrets in a vault or environment.

Useful commands:

```bash
# Rebuild and start in background
docker-compose up --build -d

# Show logs
docker-compose logs -f web

# Run a one-off shell in the web container
docker-compose run --rm web bash
```

If you want, I can also generate an `nginx` service and a `Dockerfile` variant for production with static-collection and multi-stage builds.
