from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from api.database import get_db
from src.Blog.blog_schema import BlogBase
from src.Blog.blog_service import *
from src.User.user_service import get_current_active_user

router = APIRouter()

@router.post("/blog", response_model=BlogBase)
async def create_blog(blog: BlogBase, db: Session = Depends(get_current_active_user)):
    db_blog = get_blog_by_name(db=db, name=blog.name)
    if db_blog:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Blog alread exist")
    else:
        return create_db_blog(db=db, blog=blog)
