# Development Guide — LTI App

Step-by-step guidance for local development. Stack: **React + Vite** (frontend), **Django** (backend), **PostgreSQL**, **Docker Compose** (`infra/`), per `docs/architecture.md`.

## Prerequisites

- **Python** 3.11+ (or version pinned in `backend/requirements.txt` / `pyproject.toml`)
- **Node.js** LTS and **npm** (or **pnpm** / **yarn** if the frontend lockfile standardizes on one)
- **Docker** and **Docker Compose** (for PostgreSQL and optional full stack)
- **Git**

## Repository layout

```text
lti-app/
  frontend/     # React + Vite
  backend/      # Django
  infra/        # docker-compose.yml, etc.
  docs/         # product and architecture docs
  ai-specs/     # AI specs and shared standards (see ai-specs/ai-specs/specs/)
```

Paths under `frontend/`, `backend/`, and `infra/` appear when the scaffold is generated or added.

## Environment variables

### Backend (`backend/.env` — do not commit)

Example placeholders (adjust names to match `settings.py`):

```env
DEBUG=1
SECRET_KEY=change-me-in-dev
DATABASE_URL=postgresql://lti:lti@localhost:5432/lti
# or discrete vars:
# DB_HOST=localhost
# DB_PORT=5432
# DB_NAME=lti
# DB_USER=lti
# DB_PASSWORD=lti
```

### Frontend (`frontend/.env.local` — do not commit)

```env
VITE_API_BASE_URL=http://127.0.0.1:8000
```

## Database (PostgreSQL with Docker)

From the repo root (once `infra/docker-compose.yml` exists):

```bash
docker compose -f infra/docker-compose.yml up -d
```

Verify the service is healthy per your Compose file (e.g. `docker compose ps`).

## Backend setup

```bash
cd backend
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Django typically serves at `http://127.0.0.1:8000`. Add a **`/health/`** endpoint per project conventions.

## Frontend setup

```bash
cd frontend
npm install
npm run dev
```

Vite prints the local URL (commonly `http://127.0.0.1:5173`).

## Running tests

### Backend

```bash
cd backend
python manage.py test
# or: pytest  # if pytest-django is configured
```

### Frontend

```bash
cd frontend
npm run test
# or: npm run test -- --run  # Vitest CI-style, if configured
```

## Useful references

- `docs/architecture.md` — stack and goals
- `docs/product-context.md` — product scope
- `ai-specs/ai-specs/specs/backend-standards.mdc`
- `ai-specs/ai-specs/specs/frontend-standards.mdc`
