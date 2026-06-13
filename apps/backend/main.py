#!/usr/bin/env python3
"""
FALIZ AI Backend - FastAPI Application Entry Point

This module initializes and configures the FastAPI application with:
- Middleware (CORS, RequestID, logging)
- Database connections
- Redis integration
- Plugin system
- Event handlers
"""

import logging
from contextlib import asynccontextmanager
from typing import Any

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import structlog

from config import settings
from core.database import init_db, close_db
from core.redis import init_redis, close_redis
from core.exceptions import FalizException
from core.middleware import RequestIDMiddleware, StructuredLoggingMiddleware
from routers import (
    auth,
    chat,
    voice,
    tasks,
    calendar,
    email,
    system,
    plugins,
    memory,
    events,
    health,
)

# Configure structured logging
structlog.configure(
    processors=[
        structlog.stdlib.filter_by_level,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.UnicodeDecoder(),
        structlog.processors.JSONRenderer(),
    ],
    context_class=dict,
    logger_factory=structlog.stdlib.LoggerFactory(),
    cache_logger_on_first_use=True,
)

logger = structlog.get_logger()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan context manager for application startup/shutdown.
    Handles database, Redis, and plugin initialization.
    """
    logger.info("FALIZ AI Backend Starting", version=settings.APP_VERSION)

    # Startup
    await init_db()
    await init_redis()
    logger.info("Database and Redis connections initialized")

    yield

    # Shutdown
    await close_db()
    await close_redis()
    logger.info("Database and Redis connections closed")


def create_app() -> FastAPI:
    """
    FastAPI application factory.
    Configures middleware, routes, exception handlers, and documentation.
    """
    app = FastAPI(
        title="FALIZ AI",
        description="Ultra-intelligent personal AI operating system for desktop",
        version=settings.APP_VERSION,
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
        lifespan=lifespan,
    )

    # === MIDDLEWARE ===
    # Request ID tracking
    app.add_middleware(RequestIDMiddleware)

    # Structured logging
    app.add_middleware(StructuredLoggingMiddleware)

    # CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.API_CORS_ORIGINS,
        allow_credentials=settings.API_CORS_CREDENTIALS,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # === EXCEPTION HANDLERS ===
    @app.exception_handler(FalizException)
    async def faliz_exception_handler(request: Request, exc: FalizException):
        """Handle FALIZ-specific exceptions."""
        request_id = request.state.request_id if hasattr(request.state, 'request_id') else "unknown"
        logger.error(
            "FALIZ Error",
            error=exc.error,
            message=exc.message,
            detail=exc.detail,
            request_id=request_id,
            status_code=exc.status_code,
        )
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "error": exc.error,
                "message": exc.message,
                "detail": exc.detail,
                "request_id": request_id,
            },
        )

    @app.exception_handler(Exception)
    async def general_exception_handler(request: Request, exc: Exception):
        """Handle unexpected exceptions."""
        request_id = request.state.request_id if hasattr(request.state, 'request_id') else "unknown"
        logger.exception(
            "Unhandled Exception",
            request_id=request_id,
            error_type=type(exc).__name__,
        )
        return JSONResponse(
            status_code=500,
            content={
                "error": "internal_error",
                "message": "An unexpected error occurred",
                "detail": str(exc) if settings.APP_ENV == "development" else None,
                "request_id": request_id,
            },
        )

    # === ROUTES ===
    app.include_router(health.router, tags=["Health"])
    app.include_router(auth.router, prefix="/api/v1/auth", tags=["Authentication"])
    app.include_router(chat.router, prefix="/api/v1/chat", tags=["Chat"])
    app.include_router(voice.router, prefix="/api/v1/voice", tags=["Voice"])
    app.include_router(tasks.router, prefix="/api/v1/tasks", tags=["Tasks"])
    app.include_router(calendar.router, prefix="/api/v1/calendar", tags=["Calendar"])
    app.include_router(email.router, prefix="/api/v1/email", tags=["Email"])
    app.include_router(system.router, prefix="/api/v1/system", tags=["System"])
    app.include_router(plugins.router, prefix="/api/v1/plugins", tags=["Plugins"])
    app.include_router(memory.router, prefix="/api/v1/memory", tags=["Memory"])
    app.include_router(events.router, prefix="/api/v1/events", tags=["Events"])

    # === STARTUP EVENT ===
    @app.on_event("startup")
    async def startup():
        logger.info("FastAPI application started", app_env=settings.APP_ENV)

    # === SHUTDOWN EVENT ===
    @app.on_event("shutdown")
    async def shutdown():
        logger.info("FastAPI application shutting down")

    return app


app = create_app()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app,
        host=settings.HOST,
        port=settings.PORT,
        workers=settings.WORKERS,
        log_level=settings.LOG_LEVEL.lower(),
    )
