from fastapi import APIRouter

router = APIRouter(prefix="/members", tags=["members"])

@router.post("")
def create_member_r(data):
    pass

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








