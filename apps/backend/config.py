#!/usr/bin/env python3
"""
Configuration module for FALIZ AI Backend.
All settings are loaded from environment variables with validation.
"""

from typing import List, Optional
from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    """
    Application settings with environment variable binding.
    All values are validated by Pydantic.
    """

    # === CORE ===
    APP_ENV: str = Field(default="development")
    APP_VERSION: str = Field(default="1.0.0")
    APP_NAME: str = Field(default="FALIZ AI")
    SECRET_KEY: str
    DEBUG: bool = Field(default=False)

    # === SECURITY ===
    JWT_SECRET: str
    JWT_ALGORITHM: str = Field(default="HS256")
    JWT_EXPIRE_MINUTES: int = Field(default=60)
    JWT_REFRESH_EXPIRE_DAYS: int = Field(default=30)
    ENCRYPTION_KEY: str  # base64-encoded 32-byte key

    # === DATABASE ===
    DATABASE_URL: str
    DATABASE_POOL_SIZE: int = Field(default=20)
    DATABASE_MAX_OVERFLOW: int = Field(default=10)
    DATABASE_ECHO: bool = Field(default=False)

    # === REDIS ===
    REDIS_URL: str
    REDIS_PASSWORD: Optional[str] = None
    REDIS_DB: int = Field(default=0)

    # === CHROMADB ===
    CHROMA_HOST: str = Field(default="localhost")
    CHROMA_PORT: int = Field(default=8000)
    CHROMA_COLLECTION: str = Field(default="faliz-memory")

    # === OPENAI ===
    OPENAI_API_KEY: str
    OPENAI_MODEL: str = Field(default="gpt-4o")
    OPENAI_EMBEDDING_MODEL: str = Field(default="text-embedding-3-large")
    OPENAI_TEMPERATURE: float = Field(default=0.7)
    OPENAI_MAX_TOKENS: int = Field(default=4000)

    # === ANTHROPIC ===
    ANTHROPIC_API_KEY: Optional[str] = None
    ANTHROPIC_MODEL: str = Field(default="claude-3-5-sonnet-20241022")

    # === OLLAMA ===
    OLLAMA_BASE_URL: str = Field(default="http://localhost:11434")
    OLLAMA_MODEL: str = Field(default="llama3.2")

    # === VOICE ===
    ELEVENLABS_API_KEY: Optional[str] = None
    ELEVENLABS_VOICE_ID: str = Field(default="21m00Tcm4TlvDq8ikWAM")
    ELEVENLABS_MODEL: str = Field(default="eleven_monolingual_v1")
    WHISPER_MODEL: str = Field(default="whisper-1")
    WHISPER_LANGUAGE: str = Field(default="en")
    PICOVOICE_ACCESS_KEY: Optional[str] = None

    # === GOOGLE SERVICES ===
    GOOGLE_CLIENT_ID: Optional[str] = None
    GOOGLE_CLIENT_SECRET: Optional[str] = None
    GOOGLE_REDIRECT_URI: str = Field(default="http://localhost:3000/auth/callback/google")
    GOOGLE_CALENDAR_SCOPES: str = Field(default="https://www.googleapis.com/auth/calendar")
    GMAIL_SCOPES: str = Field(default="https://mail.google.com/")
    GOOGLE_MAPS_API_KEY: Optional[str] = None

    # === EXTERNAL SERVICES ===
    OPENWEATHER_API_KEY: Optional[str] = None
    OPENWEATHER_UNITS: str = Field(default="metric")
    NEWS_API_KEY: Optional[str] = None
    WOLFRAM_ALPHA_APP_ID: Optional[str] = None
    TWILIO_ACCOUNT_SID: Optional[str] = None
    TWILIO_AUTH_TOKEN: Optional[str] = None
    TWILIO_PHONE_FROM: Optional[str] = None

    # === SPOTIFY ===
    SPOTIFY_CLIENT_ID: Optional[str] = None
    SPOTIFY_CLIENT_SECRET: Optional[str] = None
    SPOTIFY_REDIRECT_URI: str = Field(default="http://localhost:3000/auth/callback/spotify")

    # === GITHUB ===
    GITHUB_CLIENT_ID: Optional[str] = None
    GITHUB_CLIENT_SECRET: Optional[str] = None
    GITHUB_REDIRECT_URI: str = Field(default="http://localhost:3000/auth/callback/github")

    # === SMART HOME ===
    HOME_ASSISTANT_URL: Optional[str] = None
    HOME_ASSISTANT_TOKEN: Optional[str] = None
    HOME_ASSISTANT_VERIFY_SSL: bool = Field(default=True)

    # === SECURITY FEATURES ===
    FACE_AUTH_ENABLED: bool = Field(default=True)
    FACE_AUTH_CONFIDENCE: float = Field(default=0.8)
    FACE_AUTH_DETECTION_MODEL: str = Field(default="retinaface")

    # === PLUGIN FEATURE FLAGS ===
    PLUGIN_VOICE_ENABLED: bool = Field(default=True)
    PLUGIN_BRAIN_ENABLED: bool = Field(default=True)
    PLUGIN_CALENDAR_ENABLED: bool = Field(default=True)
    PLUGIN_TASKS_ENABLED: bool = Field(default=True)
    PLUGIN_COMMS_ENABLED: bool = Field(default=True)
    PLUGIN_INFO_ENABLED: bool = Field(default=True)
    PLUGIN_SYSTEM_ENABLED: bool = Field(default=True)
    PLUGIN_SMARTHOME_ENABLED: bool = Field(default=False)
    PLUGIN_VISION_ENABLED: bool = Field(default=True)
    PLUGIN_CREATE_ENABLED: bool = Field(default=True)
    PLUGIN_KNOWLEDGE_ENABLED: bool = Field(default=True)
    PLUGIN_CAREER_ENABLED: bool = Field(default=True)
    PLUGIN_ENTERTAINMENT_ENABLED: bool = Field(default=True)
    PLUGIN_LOCATION_ENABLED: bool = Field(default=True)
    PLUGIN_SECURITY_ENABLED: bool = Field(default=True)
    PLUGIN_ANALYTICS_ENABLED: bool = Field(default=True)

    # === LOGGING ===
    LOG_LEVEL: str = Field(default="INFO")
    LOG_FORMAT: str = Field(default="json")
    LOG_FILE: Optional[str] = None

    # === CELERY ===
    CELERY_BROKER_URL: str = Field(default="redis://localhost:6379/1")
    CELERY_RESULT_BACKEND: str = Field(default="redis://localhost:6379/2")
    CELERY_TIMEZONE: str = Field(default="UTC")

    # === API ===
    API_VERSION: str = Field(default="v1")
    API_RATE_LIMIT_ENABLED: bool = Field(default=True)
    API_RATE_LIMIT_REQUESTS: int = Field(default=100)
    API_RATE_LIMIT_PERIOD: int = Field(default=60)
    API_CORS_ORIGINS: List[str] = Field(
        default=["http://localhost:3000", "http://localhost:5173"]
    )
    API_CORS_CREDENTIALS: bool = Field(default=True)

    # === DEPLOYMENT ===
    HOST: str = Field(default="0.0.0.0")
    PORT: int = Field(default=8000)
    WORKERS: int = Field(default=4)
    SECURE_COOKIES: bool = Field(default=False)

    # === MONITORING ===
    SENTRY_DSN: Optional[str] = None
    SENTRY_ENVIRONMENT: str = Field(default="development")
    SENTRY_TRACES_SAMPLE_RATE: float = Field(default=0.1)

    # === URLS ===
    BACKEND_URL: str = Field(default="http://localhost:8000")
    FRONTEND_URL: str = Field(default="http://localhost:5173")

    class Config:
        env_file = ".env"
        case_sensitive = True
        extra = "allow"


# Global settings instance
settings = Settings()
