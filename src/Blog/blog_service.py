from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import Session

from Blog.blog_model import Blog, Post
from Blog.blog_schema import BlogBase


# SERVICE BLOG
def get_all_blog(db: Session):
    return db.query(Blog).all()

def get_blog_by_name(db: Session, name: str):
    db_blog = db.query(Blog).filter(Blog.name == name).first()
    return db_blog

async def create_db_blog(db: Session, blog: BlogBase):
        try:
            db_blog = Blog(
                name = blog.name,
                url = blog.url,
            )
            db.add(db_blog)
            db.commit()
            db.refresh(db_blog)
            return db_blog
        except (IntegrityError) as error:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'A database error occurred: {error.orig}')
        except SQLAlchemyError as error:
            db.rollback()
            raise HTTPException(status_code=400, detail=str(error))

def update_db_blog(db: Session, blog: BlogBase, id: int):
    db.query(Blog).filter(Blog.id == id).update(blog)
    db.commit()
    return None

# SERVICE POST
def get_all_post_from_blog(db: Session, blog_id):
    db_blog_post = db.query(Post).filter(Post.blog_id == blog_id).all()
    return db_blog_post


