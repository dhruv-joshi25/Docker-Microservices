# Docker Microservices Deployment

A production-style microservices application containerized with Docker and orchestrated using Docker Compose, with Nginx as a reverse proxy and PostgreSQL as the database.

## Architecture

Browser → Nginx (port 8080) → Frontend (HTML/Nginx)
                             → Backend (Python/Flask)
                                      → Database (PostgreSQL)

## Services

- **Nginx** — Reverse proxy, routes traffic to frontend and backend
- **Frontend** — Static HTML served via Nginx
- **Backend** — Python Flask REST API
- **Database** — PostgreSQL with persistent volume storage

## Tech Stack

- Docker and Docker Compose
- Nginx reverse proxy
- Python Flask backend API
- PostgreSQL database
- Shell scripting for automated deployment

## Setup and Run

git clone https://github.com/dhruv-joshi25/Docker-Microservices.git
cd Docker-Microservices
cp .env.example .env
./deploy.sh

## API Endpoints

GET /api/health — Backend health check
GET /api/message — Sample message from backend
GET /api/dbtest — Database connection test

## Environment Variables

POSTGRES_DB — Database name
POSTGRES_USER — Database username
POSTGRES_PASSWORD — Database password
FLASK_ENV — Flask environment
README