# app/main.py

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.utils import is_body_allowed_for_status_code
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse, Response
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_422_UNPROCESSABLE_ENTITY
from tortoise.contrib.fastapi import register_tortoise

from app.routes import plants
from app.config import tortoise_settings
from app.schemas.general import Response
from app.utils.exception import ShapeShyftException
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="Greenspace API",
    description="This is the API documentation for the Greenspace API.",
    version="1.0.0",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

BASE_PREFIX = "/api/"

app.include_router(plants.router, prefix=BASE_PREFIX + "v1/plants")

register_tortoise(
    app,
    config={
        "connections": {"default": tortoise_settings.db_connection},
        "apps": {
            "models": {
                "models": ["app.models"],
                "default_connection": "default",
            }
        },
    },
    # This will create the DB tables on startup (useful for development)
    generate_schemas=True,
    add_exception_handlers=True,
)


@app.exception_handler(ShapeShyftException)
async def shape_shyft_exception_handler(request: Request, exc: ShapeShyftException):
    return JSONResponse(
        status_code=exc.http_status_code,
        content={
            "success": False,
            "error": {"id": exc.code, "message": exc.message},
        },
    )


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(
    request: Request, exc: StarletteHTTPException
) -> Response:
    headers = getattr(exc, "headers", None)
    if not is_body_allowed_for_status_code(exc.status_code):
        return Response(status_code=exc.status_code, headers=headers)
    return JSONResponse(
        {
            "success": False,
            "error": {"id": "E1000", "message": exc.detail},
        },
        status_code=exc.status_code,
        headers=headers,
    )


@app.exception_handler(RequestValidationError)
async def request_validation_exception_handler(
    request: Request, exc: RequestValidationError
) -> JSONResponse:
    return JSONResponse(
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "success": False,
            "error": {
                "id": "E1001",
                "message": "validation_error",
                "detail": jsonable_encoder(exc.errors()),
            },
        },
    )


# on start up
@app.on_event("startup")
async def startup_event():
    pass
