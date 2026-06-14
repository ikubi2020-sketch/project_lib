from logs.logger_create import logger 
from db_connection import get_connection



class membersDB:
    def create_member(data):
        pass

    def get_all_members(): 
        pass

    def get_member_by_id(id):
        pass 

    def update_member(id, data):
        pass
        
    def deactivate_member(id):
        pass

    def activate_member(id):
        pass

    def increment_borrows(id):
        pass

    def count_active_members():
        pass

    def get_top_member():
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
