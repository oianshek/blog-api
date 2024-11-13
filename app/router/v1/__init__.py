from fastapi import APIRouter

from app.router.v1.post import router as ping_router

router = APIRouter(prefix="/v1")
router.include_router(ping_router)
