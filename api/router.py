from fastapi import APIRouter

from src.Authentication import auth_route
from src.User import user_route

router = APIRouter(
    prefix="/api/v1",
    responses={404: {"description": "Not found"}},
)

# Incluindo todas as rotas na rota principal
# router.include_router(auth_route.router, tags=['Authentication'])
router.include_router(user_route.router, tags=['User'])

@router.get("/")
async def healthchecker() -> dict:
    return {"status": "API is running"}




