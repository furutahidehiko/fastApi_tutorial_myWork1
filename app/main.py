import os
import translation

from fastapi import FastAPI, Depends
from fastapi.exceptions import RequestValidationError

from routers import router

app = FastAPI()

# app = FastAPI(dependencies=[Depends(translation.get_locale)])
# app.add_exception_handler(
#     RequestValidationError, translation.validation_exception_handler
# )


app.include_router(router.router)
