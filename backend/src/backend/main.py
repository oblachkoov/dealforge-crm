from fastapi import FastAPI

from backend.src.backend.presentation.api.v1.auth.router import router as auth_router
from backend.src.backend.presentation.api.v1.auth.router import router as user_router

app = FastAPI(
    title="DealForge CRM API",
    description="",
    version="1.0.0"
)
app.include_router(auth_router, prefix="/api/v1")
app.include_router(user_router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8008)