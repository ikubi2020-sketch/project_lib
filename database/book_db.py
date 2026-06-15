from logs.logger_create import logger 
from database.db_connection import get_connection
from utils.utils_files import run_query_dml, run_query_fetchall , run_query_fetchone
from fastapi import HTTPException


class booksDB:
    def create_book(self, data: dict):
        logger.info("active func | create_book |")
        query = "insert into books (title, author, genre, is_available) values( %s, %s, %s, %s)"
        params =  (data["title"], data["author"], data["genre"], data["is_available"])
        cursor = None
        try:
            run_query_dml(query, params)
            logger.info("book created")
            return "book created"
        except Exception as e:
            logger.error(f"reach error {e}")
            raise HTTPException(status_code=400, detail={"message" : f"reach error {e}"})
        finally :
            if cursor is not None:
                cursor.close()



    def get_all_books(self):
        logger.info("active func | get_all_books |")
        cursor = None
        query = "select title from books"
        try:
            books_list = run_query_fetchall(query)
            logger.info("all books list")
            return books_list
        except Exception as e:
            logger.error(f"reach error {e}")
            return {"message" : f"reach error {e}"}
        finally:
            if cursor is not None:
                cursor.close()


    def get_book_by_id(self, id):
        logger.info("active func | get_book_by_id |")
        cursor = None
        param = (id,)
        query = "select * from books where id = %s"
        try:
            book = run_query_fetchone(query, param)
            logger.info("send book outside")
            return book
        except Exception as e:
            logger.error(f"reach error {e}")
            raise HTTPException (status_code=400, detail={"message" : f"reach error {e}"})
        finally:
            if cursor is not None:
                cursor.close()


    def update_book(self, id, data):
        pass 
    
    def set_available(self, id, val, member_id):
        pass

    def count_total_books(self):
        pass

    def count_available_books(self):
        pass

    def count_borrowed_books(self):
        pass

    def count_by_genre(self, genre):
        pass
    
    def count_active_borrows_by_member(self, member_id):
        pass




def ______():
    logger.info("active func |  |")
    cursor = None
    try:
        logger.info("")

    except Exception as e:
        logger.error(f"reach error {e}")
        raise HTTPException (status_code=400, detail={"message" : f"reach error {e}"})
    finally:
        if cursor is not None:
            cursor.close()
