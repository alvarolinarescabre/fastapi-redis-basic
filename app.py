from fastapi import FastAPI, HTTPException
from redis import Redis, RedisError
import os

app = FastAPI()

# Initialize Redis connection
redis_client = Redis(
    host=os.getenv("REDIS_HOST", "cache"),
    port=int(os.getenv("REDIS_PORT", "6379")),
    db=int(os.getenv("REDIS_DB", "0")),
    decode_responses=True  # Automatically decode bytes to str
)

@app.get("/")
async def index():
    """Increment visit counter and return updated value."""
    try:
        visits = redis_client.incr("visits")
        return {"visits": visits}
    except RedisError:
        raise HTTPException(status_code=500, detail="Error connecting to Redis")

@app.get("/visits")
async def total_visits():
    """Return total visits without incrementing the counter."""
    try:
        count = redis_client.get("visits")
        total = int(count) if count is not None else 0
        return {"total_visits": total}
    except RedisError:
        raise HTTPException(status_code=500, detail="Error connecting to Redis")

@app.get("/health")
async def health_check():
    """Health check endpoint to verify Redis connectivity."""
    try:
        redis_client.ping()
        return {"status": "healthy", "redis": "connected"}
    except RedisError:
        raise HTTPException(status_code=503, detail="Redis unavailable")