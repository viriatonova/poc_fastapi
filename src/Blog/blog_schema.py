from datetime import datetime

from pydantic import BaseModel, ConfigDict


class BlogBase(BaseModel):
    id: int | None = None
    name: str
    url: str
     
class PostIn(BaseModel):
    id: int | None = None
    author_id: int
    blog_id: int
    title: str
    subtitle: str
    summary: str | None = None
    content: str
    slug: str
    is_published: bool | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None

class PostOut(BaseModel):
    author_id: int
    blog_id: int
    title: str
    subtitle: str
    summary: str | None = None
    content: str
    slug: str
    is_published: bool | None = None
    created_at: datetime | None = None
        
class CommentBase(BaseModel):
    id: int | None = None
    post_id: int
    comment: str

class TagBase(BaseModel):
    id: int | None = None
    name: str
    slug: str | None = None

class PostTagBase(BaseModel):
    id: int | None = None
    tag_id: int 
    post_id: int

class CategoryBase(BaseModel):
    id: int | None = None
    name: str
    slug: str | None = None

class PostCategoryBase(BaseModel):
    id: int | None = None
    category_id: int 
    post_id: int
