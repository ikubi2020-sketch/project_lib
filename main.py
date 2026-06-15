
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from logs.logger_create import logger
from routers.book_routes import router as books_router
from routers.members_routes import router as members_router
from routers.reports_routes import router as reports_routes

app = FastAPI(responses={400: {"description": "Validation Error -  in valid details"}})

app.include_router(books_router)
app.include_router(members_router)
app.include_router(reports_routes)
 

@app.exception_handler(RequestValidationError)
def wrong_details(_request, exe : RequestValidationError):
    logger.error(f"error in details {exe.errors()}")
    return JSONResponse (status_code = 400 , content ={"error" : exe.errors()} )