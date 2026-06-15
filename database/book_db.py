from logs.logger_create import logger 
from database.db_connection import get_connection
from utils.utils_files import run_query_dml, run_query_fetchall , run_query_fetchone
from fastapi import HTTPException


class booksDB:
    def create_book(self, data: dict):
        logger.info("active func | create_book |")
        query = "insert into books (title, author, genre, is_available) values( %s, %s, %s)"
        params =  (data["title"], data["author"], data["genre"])
        try:
            run_query_dml(query, params)
            logger.info("book created")
            return "book created"
        except Exception as e:
            logger.error(f"reach error {e}")
            raise HTTPException(status_code=400, detail={"message" : f"reach error {e}"})
        

    def get_all_books(self):
        logger.info("active func | get_all_books |")
        query = "select title from books"
        try:
            books_list = run_query_fetchall(query)
            logger.info("all books list")
            return books_list
        except Exception as e:
            logger.error(f"reach error {e}")
            return {"message" : f"reach error {e}"}
        

    def get_book_by_id(self, id):
        logger.info("active func | get_book_by_id |")
        param = (id,)
        query = "select * from books where id = %s"
        try:
            book = run_query_fetchone(query, param)
            logger.info("send book outside")
            return book
        except Exception as e:
            logger.error(f"reach error {e}")
            raise HTTPException (status_code=400, detail={"message" : f"reach error {e}"})
        
    def update_book(self, id, data):
        logger.info("active func | update_book |")
        param = (data["title"], data["author"], data["genre"], id) 
        query = "update  books  set title = %s, author = %s, genre = %s where id = %s;" 
        try:
            run_query_dml(query , param)
            logger.info("update book")
            return "updated book"
        except Exception as e:
            logger.error(f"reach error {e}")
            raise HTTPException (status_code=400, detail={"message" : f"reach error {e}"})
        
        
    def set_available(self, id, val, member_id):
        logger.info("active func | set_available |")
        query = ""
        try:

            logger.info("")
        except Exception as e:
            logger.error(f"reach error {e}")
            raise HTTPException (status_code=400, detail={"message" : f"reach error {e}"})
        
    def count_total_books(self):
        logger.info("active func | count_total_books |")
        query = "select count(title) as totally from books;"
        try:
            count_books = run_query_fetchone(query)
            logger.info("count of books sent out")
            return count_books
        except Exception as e:
            logger.error(f"reach error {e}")
            raise HTTPException (status_code=400, detail={"message" : f"reach error {e}"})
        

    def count_available_books(self):
        logger.info("active func | count_available_books |")
        query = "select count(*) as available from books  where is_available is True;"
        try:
            available = run_query_fetchone(query)
            logger.info("count of available books sent out")
            return available
        except Exception as e:
            logger.error(f"reach error {e}")
            raise HTTPException (status_code=400, detail={"message" : f"reach error {e}"})
        

    def count_borrowed_books(self):
        logger.info("active func | count_borrowed_books |")
        query = "select count(*) as unavailable from books  where is_available is False;"
        try:
            unavailable = run_query_fetchone(query)
            logger.info("sent borrowed books")
            return unavailable
        except Exception as e:
            logger.error(f"reach error {e}")
            raise HTTPException (status_code=400, detail={"message" : f"reach error {e}"})
        

    def count_by_genre(self, genre:str):
        logger.info("active func | count_by_genre |")
        param = (genre,)
        query = "select count(*) as my_genre from books where genre = %s;"
        try:
            genre_count = run_query_fetchone(query, param)
            logger.info("return count by genre")
            return genre_count
        except Exception as e:
            logger.error(f"reach error {e}")
            raise HTTPException (status_code=400, detail={"message" : f"reach error {e}"})
        

    
    def count_active_borrows_by_member(self, member_id):
        logger.info("active func | count_active_borrows_by_member |")
        param = (member_id,)
        query = "select total_borrows from members where id = %s;"
        try:
            borrows_num = run_query_fetchone(query, param)
            logger.info("borrow number sent out")
            return borrows_num
        except Exception as e:
            logger.error(f"reach error {e}")
            raise HTTPException (status_code=400, detail={"message" : f"reach error {e}"})



