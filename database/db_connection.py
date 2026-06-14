import mysql.connector
from logs.logging import logger


def get_connection():
    connection = None
    connection =mysql.connector.connect(
    host="localhost",
    port=3306,
    password=1313,
    user="root",
    database="library_db")
    return connection 




def create_table_books():
    logger.info("active func | create_table |")
    cursor = None
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(
            """
                create table if not exists books,
                id int primary key auto_increment,
                title varchar(50) not null,
                genre varchar(20) not null,
                is_available boolean not null,
                borrowed_by_member_id default null;
            """)
    except Exception as e:
        logger.error(f"reach error {e}")
        return {"message" : f"reach error {e}"}
    finally:
        if cursor is not None:
            cursor.close()







