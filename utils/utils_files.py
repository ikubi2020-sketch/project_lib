from pydantic import BaseModel,  Field
from database.db_connection import get_connection
from logs.logger_create import logger

class members(BaseModel):
    pass



def run_query(query, params = None):
    connection = None
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(query, params)
    connection.commit()
    if cursor is not None:
        cursor.close()


def run_query_fetchall(query, params = None):
    connection = None
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(query, params)
    result = cursor.fetchall()
    if cursor is not None:
        cursor.close()
    return result


def run_query_fetchone(query, params = None):
    connection = None
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(query, params)
    result = cursor.fetchall()
    if cursor is not None:
        cursor.close()
    return result


def ______():
    logger.info("active func |  |")
    cursor = None
    try:
        logger.info("")
    except Exception as e:
        logger.error(f"reach error {e}")
        return {"message" : f"reach error {e}"}
    

