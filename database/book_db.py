from logs.logger_create import logger 
from database.db_connection import get_connection
from utils.utils_files import run_query, run_query_fetchall
from fastapi import HTTPException


class booksDB:
    def create_book(self, data: dict):
        logger.info("active func | create_book |")
        query = "insert into books values( %s, %s, %s, %s)"
        params =  (data["title"], data["author"], data["genre"], data["is_available"])
        try:
            run_query(query, params)
        except Exception as e:
            logger.error(f"reach error {e}")
            raise HTTPException(status_code=400, detail={"message" : f"reach error {e}"})

    def get_all_books():
        pass 

    def get_book_by_id(id):
        pass

    def update_book(id, data):
        pass 
    
    def set_available(id, val, member_id):
        pass

    def count_total_books():
        pass

    def count_available_books():
        pass

    def count_borrowed_books():
        pass

    def count_by_genre(genre):
        pass
    
    def count_active_borrows_by_member(member_id):
        pass




def ______():
    logger.info("active func |  |")
    cursor = None
    try:
        logger.info("")
    except Exception as e:
        logger.error(f"reach error {e}")
        return {"message" : f"reach error {e}"}
    

