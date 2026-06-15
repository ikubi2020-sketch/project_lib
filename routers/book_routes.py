from fastapi import  APIRouter
from database.book_db import *
from utils.utils_files import * 

books_class = booksDB()

router = APIRouter(prefix="/book", tags=["books"])

@router.post("")
def create_book_r(data : Book):
    logger.info("active func  | create_book_r |")
    new_data = data.model_dump()
    result = books_class.create_book(new_data)
    return {"status_code" : 200, "result" : result}
   

@router.get("")
def get_all_books_r():
    logger.info("active func  | get_all_books_r |")
    books = books_class.get_all_books() 
    return {"status_code" : 200, "result" : books}

@router.get("/{id}")
def get_book_by_id_r(id):
    logger.info("active func  | get_book_by_id_r |")
    book = books_class.get_book_by_id(id)
    return {"status_code" : 200, "result" : book}

@router.put("/{id}")
def update_book_r(id : int, data : Book):
    new_data = dict(data)
    logger.info("active func | update_book_r |")
    result = books_class.update_book(id, new_data)
    return   {"status_code" : 200, "result" : result}


@router.put("/{id}/return/{member_id}")
def set_available_r(id, val, member_id):
    pass

@router.put("/{id}/borrow/{member_id}")
def set_available_r(id, val, member_id):
    pass

