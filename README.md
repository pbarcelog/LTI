# LTI App

## Overview
LTI is a recruitment management platform that supports the hiring process from job creation to candidate selection.

This project is a minimal full-stack skeleton created as part of a Spec-Driven Development exercise.

The goal of this phase is to ensure that:
- frontend, backend, and database are properly set up
- all services can start without errors

No business functionality is implemented yet.

---

## Tech Stack

- **Frontend**: React + Vite  
- **Backend**: Django  
- **Database**: PostgreSQL  
- **Infrastructure**: Docker Compose  

---

## Project Structure

```text
lti-app/
  frontend/        # React application
  backend/         # Django backend
  infra/
    docker-compose.yml
  docs/
    product-context.md
    data-model.md
    architecture.md
```

---

## Verification (Docker Compose)

From the repository root:

### Start everything
```bash
docker compose -f infra/docker-compose.yml up -d --build
```

### Check backend health endpoint
```powershell
Invoke-RestMethod -Uri http://localhost:8000/health/
```

You should see JSON containing:
```json
{ "status": "ok", "service": "lti-backend" }
```

### Check frontend
Open `http://localhost:5173/` in your browser and verify you see:
`Hello LTI`

### Stop services
```bash
docker compose -f infra/docker-compose.yml down -v
```