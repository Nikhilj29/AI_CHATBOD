from fastapi import APIRouter

router = APIRouter()

@router.get("/all")
def get_all_users():
    return "ALL USERS"