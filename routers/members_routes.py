from fastapi import APIRouter
from utils.utils_files import *
from database.member_db import * 
from logs.logger_create import logger 


router = APIRouter(prefix="/members", tags=["members"])

db_class = membersDB()

@router.post("")
def create_member_r(data : Members):
    logger.info("active func | create_member_r |")
    new_data = data.model_dump()
    result = db_class.create_member(new_data)
    return {"status code" : 200 ,"result" : result}

@router.get("")
def get_all_members_r():
    
    pass

@router.get("/{id}")
def get_member_by_id(id):
    pass 

@router.put("/{id}")
def update_member(id, data):
    pass

@router.put("/{id}/deactivate")
def deactivate_member(id):
    pass

@router.put("/{id}/activate")
def activate_member(id):
    pass

@router.put("/books/{id}/borrow/{member_id}")
def increment_borrows(id):
    pass



