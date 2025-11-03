# goto — Django backend scaffold

Este repo añade un backend Django mínimo para exponer APIs que consuma la PWA Gotogym.

Requisitos:
- Docker y docker-compose (opcional) o Python 3.11+ y pip.

Levantar con Docker (opcional):
1. docker-compose build
2. docker-compose up -d
3. Acceder a http://localhost:8000/api/ping

Levantar local sin Docker:
1. python -m venv .venv
2. source .venv/bin/activate
3. pip install -r requirements.txt
4. cd backend
5. python manage.py migrate
6. python manage.py createsuperuser
7. python manage.py runserver

Endpoints de ejemplo:
- POST /api/auth/token/        -> { "username","password" } -> obtiene access y refresh tokens
- POST /api/auth/token/refresh/-> renovar token
- POST /api/auth/register/     -> registro rápido de usuario (dev)
- GET  /api/ping/              -> { "ping": "pong" }
- /api/members/                -> CRUD del recurso Member (requiere autenticación para POST/PUT/DELETE por defecto)

Notas:
- Configuración de database lee DATABASE_URL para Postgres/SQLite; por defecto usa SQLite.
- Ajustar CORS_ALLOWED_ORIGINS usando la variable de entorno CORS_ALLOWED_ORIGINS (separa por espacios).
- Para la PWA: usar el endpoint /api/auth/token/ para obtener el JWT y agregar Authorization: Bearer <token> en las solicitudes.
