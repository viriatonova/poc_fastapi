from fastapi import APIRouter, status

router = APIRouter()

@router.post("/singin", status_code=status.HTTP_200_OK)
def sing_in():
    pass
