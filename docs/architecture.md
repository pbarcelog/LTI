# Architecture – LTI App

## Goal
Provide a minimal full-stack project skeleton for the LTI application.

The system must include:
- frontend
- backend
- database

All components must be able to start correctly.
No business functionality is implemented at this stage.

---

## Technology Choices

### Frontend
- React
- Vite

**Reason**
- Fast and simple setup
- Lightweight development server
- Suitable for a minimal UI (e.g. "Hello LTI")

---

### Backend
- Django

**Reason**
- Quick project scaffolding
- Built-in ORM and structure
- Easy integration with PostgreSQL
- Minimal configuration required to get running

---

### Database
- PostgreSQL

**Reason**
- Real database service (not embedded like SQLite)
- Works well with Docker Compose
- Suitable for future scalability

---

### Infrastructure
- Docker Compose

**Reason**
- Simple orchestration of services
- Allows running frontend, backend, and database together
- Reproducible local environment

---

## High-Level Architecture

```text
[ Frontend (React) ]  →  [ Backend (Django API) ]  →  [ PostgreSQL DB ]