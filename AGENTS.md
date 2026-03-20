# Agents Configuration – LTI App

## Base Standards
Follow the shared AI development standards defined in:

- ai-specs/ai-specs/specs/base-standards.mdc

---

## Project Context

This project is a minimal full-stack skeleton for the LTI application.

LTI is a recruitment management platform that supports:
- job creation
- application tracking
- candidate evaluation
- hiring decisions

The goal of this phase is:
- to scaffold frontend, backend, and database
- to ensure all services can start correctly

No business functionality is implemented yet.

---

## Project Documentation

Before making any changes, review:

- docs/product-context.md
- docs/data-model.md
- docs/architecture.md

These documents define the system context and constraints.

---

## Project Structure

- frontend/ → React application
- backend/ → Django backend
- infra/ → Docker configuration
- docs/ → project documentation
- ai-specs/ → shared AI rules and agents

---

## Instructions for Agents

- Keep implementations minimal and functional
- Do not add unnecessary complexity
- Do not invent features not described in the docs
- Ensure all components can start without errors
- Prefer simple and clear solutions

---

## Current Objective

Scaffold a minimal working system with:

- React frontend (Hello LTI page)
- Django backend (health endpoint)
- PostgreSQL database
- Docker Compose setup

The system must be runnable locally without errors.