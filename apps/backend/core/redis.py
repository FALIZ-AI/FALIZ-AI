#!/usr/bin/env python3
"""
Redis connection management for caching and pub/sub.
"""

import structlog
import aioredis
from redis.asyncio.connection import ConnectionPool

from config import settings

logger = structlog.get_logger()

redis_client = None


async def init_redis() -> None:
    """Initialize Redis connection pool."""
    global redis_client

    try:
        redis_client = await aioredis.from_url(
            settings.REDIS_URL,
            password=settings.REDIS_PASSWORD,
            db=settings.REDIS_DB,
            encoding="utf8",
            decode_responses=True,
            retry_on_timeout=True,
        )
        await redis_client.ping()
        logger.info("Redis connection established")
    except Exception as exc:
        logger.exception("Failed to connect to Redis", error=str(exc))
        raise


async def close_redis() -> None:
    """Close Redis connection."""
    if redis_client:
        await redis_client.close()
        logger.info("Redis connection closed")


def get_redis():
    """Get Redis client instance."""
    if not redis_client:
        raise RuntimeError("Redis not initialized")
    return redis_client
