from logs.logger_create import logger 
from database.db_connection import get_connection
from utils.utils_files import *
from fastapi import HTTPException

class membersDB:
    def create_member(self, data):
        logger.info("active func | create_member |")
        cursor = None
        params =  (data["name"], data["email"], data["is_active"], data["total_borrows"])
        query = "insert into members (name,email, is_active, total_borrows) values   (%s, %s,  %s, %s);" 
        try:
            run_query_dml(query, params)
            logger.info("crete member")
        except Exception as e:
            logger.error(f"reach error {e}")
            raise HTTPException (status_code=400, detail={"message" : f"reach error {e}"})
       

    def get_all_members(self): 
        pass

    def get_member_by_id(self, id):
        pass 

    def update_member(self, id, data):
        pass
        
    def deactivate_member(self, id):
        pass

    def activate_member(self, id):
        pass

    def increment_borrows(self, id):
        pass

    def count_active_members(self):
        pass

    def get_top_member(self):
        pass


def ______():
    logger.info("active func |  |")
    cursor = None
    try:
        logger.info("")
    except Exception as e:
        logger.error(f"reach error {e}")
        # raise HTTPException (status_code=400, detail={"message" : f"reach error {e}"})
    

