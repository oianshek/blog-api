from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse

from app.core import settings
from app.exception import DatabaseErrorException
from app.router import router

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.PROJECT_VERSION,
)


@app.get("/", include_in_schema=False)
async def docs_redirect():
    return RedirectResponse(url="/docs")


@app.exception_handler(DatabaseErrorException)
async def sql_alchemy_exception(request, exc: DatabaseErrorException):
    raise HTTPException(
        status_code=400,
        detail=exc.detail
    )

app.include_router(router)
