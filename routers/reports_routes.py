from fastapi import APIRouter
from database.book_db import booksDB
from utils.utils_files import logger

class_books = booksDB()

router = APIRouter(prefix="/reports", tags=["reports"])

@router.get("/members/summery")
def count_active_members():
    pass

@router.get("/members/top-member ")
def get_top_member():
    pass

@router.get("/books/summery")
def count_total_books_r():
    logger.info("active func | count_total_books_r |")
    all_books = class_books.count_total_books()
    return {"status" : 200, "result" : all_books}


@router.get("/books/summery-available")
def count_available_books():
    logger.info("active func | count_available_books |")
    available_books = class_books.count_available_books()
    return {"status" : 200, "result" : available_books}

    

@router.get("books/summery-unaveil")
def count_borrowed_books():
    logger.info("active func | count_available_books |")
    unavailable_books = class_books.count_borrowed_books()
    return {"status" : 200, "result" : unavailable_books}

@router.get("/books-by-genre")
def count_by_genre_r(genre : str):
    logger.info("active func | count_by_genre_r |")
    count_genre = class_books.count_by_genre(genre)
    return {"status" : 200, "result" : count_genre}

@router.get("/books/borrow/{member_id}")
def count_active_borrows_by_member(member_id : int):
    logger.info("active func | count_active_borrows_by_member |")
    borrow_num = class_books.count_active_borrows_by_member(member_id)
    return {"status" : 200, "result" : borrow_num}



