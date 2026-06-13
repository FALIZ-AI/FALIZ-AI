.PHONY: help dev build test lint format clean docker-build docker-up docker-down migrate seed

# Colors for output
RED=\033[0;31m
GREEN=\033[0;32m
YELLOW=\033[1;33m
NC=\033[0m # No Color

help:
	@echo "$(GREEN)FALIZ AI - Development Makefile$(NC)"
	@echo ""
	@echo "$(YELLOW)Development:$(NC)"
	@echo "  make dev              Start development environment (Docker Compose)"
	@echo "  make dev-frontend     Start frontend dev server (Vite)"
	@echo "  make dev-backend      Start backend dev server (Uvicorn)"
	@echo ""
	@echo "$(YELLOW)Testing:$(NC)"
	@echo "  make test             Run all tests"
	@echo "  make test-backend     Run backend tests only"
	@echo "  make test-frontend    Run frontend tests only"
	@echo "  make coverage         Generate coverage report"
	@echo ""
	@echo "$(YELLOW)Code Quality:$(NC)"
	@echo "  make lint             Lint code"
	@echo "  make format           Format code (black + prettier)"
	@echo "  make type-check       Run type checkers (mypy + tsc)"
	@echo ""
	@echo "$(YELLOW)Docker:$(NC)"
	@echo "  make docker-build     Build Docker images"
	@echo "  make docker-up        Start Docker Compose"
	@echo "  make docker-down      Stop Docker Compose"
	@echo "  make docker-logs      View Docker logs"
	@echo ""
	@echo "$(YELLOW)Database:$(NC)"
	@echo "  make migrate          Run database migrations"
	@echo "  make migrate-create   Create new migration"
	@echo "  make seed             Seed test data"
	@echo ""
	@echo "$(YELLOW)Cleanup:$(NC)"
	@echo "  make clean            Remove build artifacts"
	@echo "  make clean-all        Remove everything (containers, volumes, etc.)"

# Development
dev:
	@echo "$(GREEN)Starting FALIZ AI development environment...$(NC)"
	docker-compose -f docker-compose.yml up -d
	@echo "$(GREEN)Backend: http://localhost:8000$(NC)"
	@echo "$(GREEN)API Docs: http://localhost:8000/docs$(NC)"
	@echo "$(GREEN)Waiting for services to be healthy...$(NC)"
	@sleep 5
	@docker-compose ps

dev-frontend:
	@echo "$(GREEN)Starting frontend dev server...$(NC)"
	cd apps/frontend && npm run dev

dev-backend:
	@echo "$(GREEN)Starting backend dev server...$(NC)"
	cd apps/backend && python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Testing
test: test-backend test-frontend
	@echo "$(GREEN)All tests passed!$(NC)"

test-backend:
	@echo "$(GREEN)Running backend tests...$(NC)"
	cd apps/backend && python -m pytest tests/ -v --tb=short

test-frontend:
	@echo "$(GREEN)Running frontend tests...$(NC)"
	cd apps/frontend && npm run test

coverage:
	@echo "$(GREEN)Generating coverage report...$(NC)"
	cd apps/backend && python -m pytest tests/ --cov=. --cov-report=html
	@echo "$(GREEN)Coverage report: apps/backend/htmlcov/index.html$(NC)"

# Code Quality
lint:
	@echo "$(GREEN)Linting Python code...$(NC)"
	cd apps/backend && python -m pylint faliz_* main.py || true
	@echo "$(GREEN)Linting TypeScript code...$(NC)"
	cd apps/frontend && npm run lint || true

format:
	@echo "$(GREEN)Formatting Python code...$(NC)"
	cd apps/backend && python -m black . && python -m isort .
	@echo "$(GREEN)Formatting TypeScript code...$(NC)"
	cd apps/frontend && npm run format

type-check:
	@echo "$(GREEN)Type checking Python...$(NC)"
	cd apps/backend && python -m mypy . --ignore-missing-imports || true
	@echo "$(GREEN)Type checking TypeScript...$(NC)"
	cd apps/frontend && npm run type-check

# Docker
docker-build:
	@echo "$(GREEN)Building Docker images...$(NC)"
	docker-compose build

docker-up:
	@echo "$(GREEN)Starting Docker Compose...$(NC)"
	docker-compose up -d

docker-down:
	@echo "$(GREEN)Stopping Docker Compose...$(NC)"
	docker-compose down

docker-logs:
	@echo "$(GREEN)Tailing Docker logs...$(NC)"
	docker-compose logs -f

# Database
migrate:
	@echo "$(GREEN)Running database migrations...$(NC)"
	cd apps/backend && alembic upgrade head

migrate-create:
	@echo "$(YELLOW)Enter migration name:$(NC)"
	@read name; cd apps/backend && alembic revision --autogenerate -m "$$name"

seed:
	@echo "$(GREEN)Seeding test data...$(NC)"
	cd apps/backend && python scripts/seed.py

# Build
build:
	@echo "$(GREEN)Building for production...$(NC)"
	cd apps/frontend && npm run build
	cd apps/backend && python -m pip install --upgrade pip setuptools wheel

install:
	@echo "$(GREEN)Installing dependencies...$(NC)"
	cd apps/frontend && npm install
	cd apps/backend && python -m pip install -r requirements.txt
	@echo "$(GREEN)Dependencies installed!$(NC)"

# Cleanup
clean:
	@echo "$(GREEN)Cleaning build artifacts...$(NC)"
	cd apps/frontend && rm -rf node_modules dist build
	cd apps/backend && find . -type d -name __pycache__ -exec rm -r {} + 2>/dev/null || true
	rm -rf build dist *.egg-info

clean-all: clean
	@echo "$(GREEN)Removing Docker containers and volumes...$(NC)"
	docker-compose down -v

.PHONY: help dev dev-frontend dev-backend test test-backend test-frontend coverage lint format type-check docker-build docker-up docker-down docker-logs migrate migrate-create seed build install clean clean-all
