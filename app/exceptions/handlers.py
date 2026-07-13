from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse

from app.dto.error import ErrorResponse


def register_exception_handlers(app: FastAPI):

    @app.exception_handler(Exception)
    async def global_exception_handler(
        request: Request,
        exc: Exception,
    ):

        response = ErrorResponse(
            error_code="INTERNAL_SERVER_ERROR",
            message=str(exc),
        )

        return JSONResponse(
            status_code=500,
            content=response.model_dump(),
        )