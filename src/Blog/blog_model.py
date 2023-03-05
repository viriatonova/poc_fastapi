from sqlalchemy import (Boolean, Column, DateTime, ForeignKey, Integer, String,
                        func)

from api.database import BASE

class Blog(BASE):
    __tablename__ = "blog"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    url = Column(String(255))
    
class Post(BASE):
    __tablename__ = "post"
    
    id = Column(Integer, primary_key=True, index=True)
    author_id = Column(Integer, ForeignKey("user.id"), index=True)
    blog_id = Column(Integer, ForeignKey("blog.id"), index=True)
    title = Column(String(255))
    subtitle = Column(String(255))
    summary = Column(String(255))
    content = Column(String(255))
    slug = Column(String(255))
    is_published = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), nullable=False, default=func.now())
    updated_at = Column(DateTime(timezone=True), nullable=True)

class Comment(BASE):
    __tablename__ = "comment"

    id = Column(Integer, primary_key=True, index=True)
    post_id = Column(Integer, ForeignKey("post.id"), index=True)
    comment = Column(String(1200))

class Tag(BASE):
    __tablename__ = "tag"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    slug = Column(String(255))

class PostTag(BASE):
    __tablename__ = "post_tag"
    
    id = Column(Integer, primary_key=True, index=True)
    tag_id = Column(Integer, ForeignKey("tag.id"), index=True)
    post_id = Column(Integer, ForeignKey("post.id"), index=True)


class Category(BASE):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    slug = Column(String(255))

class PostCategory(BASE):
    __tablename__ = "post_category"

    id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer, ForeignKey("category.id"), index=True)
    post_id = Column(Integer, ForeignKey("post.id"), index=True)


