from fastapi import APIRouter, status

router = APIRouter()

@router.post("/singup", status_code=status.HTTP_200_OK)
def sing_up():
    pass

