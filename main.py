
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from database.db_connection import *
from logs.logger_create import logger
from database.book_db import booksDB
from routers.book_routes import router as books_router
from routers.members_routes import router as members_router
from routers.reports_routes import router as reports_routes

app = FastAPI()

app.include_router(books_router)
app.include_router(members_router)
app.include_router(reports_routes)

