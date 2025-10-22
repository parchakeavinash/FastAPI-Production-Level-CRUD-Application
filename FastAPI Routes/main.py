from contextlib import asynccontextmanager
from fastapi import FastAPI, APIRouter
from routers.items import router as items_router
from routers.automation import router as automations_router
from routers.limiter import limiter
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded


#asynccontextmanager → used to define startup and shutdown logic (lifespan) in FastAPI.
async def lifespan(app:FastAPI):
    print("🚀 Application starting up...")
    # Initialize connections, load models, etc.
    yield
    print("🛑 Application shutting down...")


# create FastAPI app
app = FastAPI(
    title="Learning FastAPI API",
    description="Production-ready FastAPI application",
    version="1.0.0",
    lifespan=lifespan
)

# Additional test router
test_router = APIRouter(tags=["test"])

@test_router.get("/posts")
async def posts():
    return {"posts": "test data"}

# include all the router
app.include_router(items_router)
app.include_router(automations_router)
app.include_router(test_router)

# Setup rate limiting
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# Root endpoint
@app.get("/", tags=["health"])
def read_root():
    return {
        "message": "Server is running",
        "status": "healthy",
        "version": "1.0.0"
    }
