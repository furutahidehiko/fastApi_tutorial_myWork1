# from fastapi import Request
# from fastapi.exceptions import RequestValidationError
# from pydantic_i18n import PydanticI18n
# from starlette.responses import JSONResponse
# from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

# from pydantic_messages import translations


# __all__ = ["get_locale", "validation_exception_handler"]

# DEFAULT_LOCALE = "ja_JP"

# tr = PydanticI18n(translations)


# def get_locale(locale: str = DEFAULT_LOCALE) -> str:
#     return locale


# async def validation_exception_handler(
#     request: Request, exc: RequestValidationError
# ) -> JSONResponse:
#     current_locale = request.query_params.get("locale", DEFAULT_LOCALE)
#     return JSONResponse(
#         status_code=HTTP_422_UNPROCESSABLE_ENTITY,
#         content={"detail": tr.translate(exc.errors(), current_locale)},
#     )
