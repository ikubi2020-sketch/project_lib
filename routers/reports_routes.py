from fastapi import APIRouter


router = APIRouter(prefix="/reports", tags=["reports"])

@router.get("/members/summery")
def count_active_members():
    pass

@router.get("/members/top-member ")
def get_top_member():
    pass

@router.get("/books/summery")
def count_total_books():
    pass

@router.get("/books/summery-available")
def count_available_books():
    
    pass

@router.get("books/summery-unaveil")
def count_borrowed_books():
    pass

@router.get("/books-by-genre")
def count_by_genre(genre):
    pass

@router.get("/books/{id}/borrow/{member_id}")
def count_active_borrows_by_member(id : int, member_id : int):
    pass 


