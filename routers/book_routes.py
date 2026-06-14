from fastapi import  APIRouter

router = APIRouter(prefix="/book", tags=["books"])

@router.post("")
def create_book_r(data):
    pass

@router.get("")
def get_all_books_r(): 
    pass

@router.get("/{id}")
def get_book_by_id_r(id):
    pass

@router.put("/{id}")
def update_book_r(id, data):
    pass

@router.put("/{id}/return/{member_id}")
def set_available_r(id, val, member_id):
    pass

@router.put("/{id}/borrow/{member_id} ")
def set_available_r(id, val, member_id):
    pass

