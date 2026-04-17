from fastapi import FastAPI

from app.api.admin_api import router as admin_router
from app.api.guest_api import router as guest_router
from app.api.traveler_api import router as traveler_router

app = FastAPI()
app.include_router(guest_router)
app.include_router(traveler_router)
app.include_router(admin_router)


@app.get('/health')
def health() -> dict[str, str]:
    return {'status': 'ok'}
