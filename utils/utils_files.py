from pydantic import BaseModel,  Field
from database.db_connection import get_connection
from logs.logger_create import logger

class Members(BaseModel):
    name : str = Field(min_length= 1, max_length=50)
    email : str = Field(min_length= 1, max_length=100)
    is_active : bool 
    total_borrows : int


class book(BaseModel):
    title : str = Field(min_length=2, max_length=50)
    author : str = Field(min_length=2, max_length=50)
    genre : str = Field(min_length=2, max_length=50)
    is_available : bool
    

def run_query_dml(query, params = None):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(query, params)
    connection.commit()
    if cursor is not None:
        cursor.close()


def run_query_fetchall(query, params = None):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(query, params)
    result = cursor.fetchall()
    return result


def run_query_fetchone(query, params = None):
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(query, params)
    result = cursor.fetchone()
    return result


def ______():
    logger.info("active func |  |")
    cursor = None
    try:
        logger.info("")

    except Exception as e:
        logger.error(f"reach error {e}")
        # raise HTTPException (status_code=400, detail={"message" : f"reach error {e}"})
    

