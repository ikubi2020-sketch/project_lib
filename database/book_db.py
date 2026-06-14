from logs.logger_create import logger 
from db_connection import get_connection


class booksDB:
    def create_book(data):
        pass

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
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(";")
    except Exception as e:
        logger.error(f"reach error {e}")
        return {"message" : f"reach error {e}"}
    finally:
        if cursor is not None:
            cursor.close()
