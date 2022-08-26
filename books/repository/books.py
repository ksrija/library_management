from sqlalchemy.orm import Session
from .. import  schemas
from fastapi import HTTPException, status
# from ..dependency import users
from ..db import collection_book

# from bson import ObjectId


def get_all():
    blogs = list(collection_book.find())
    return blogs

# # does not make sense for books
# def get_profile(db: Session):
#     blogs = db.query(models.Blog).filter(
#         models.Blog.user_id == users.user_id).all()
#     print(blogs)
#     return blogs


def create(request: schemas.Books):
    data = dict(request)
    # data["user_id"] = str(users.user_id)
    collection_book.insert_one(data)
    return request


# def destroy(id: str, db: Session):
#     blog = db.query(models.Blog).filter(models.Blog.id == id)
#     blog = collection_name.find_one({"_id": ObjectId(id)})
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"Blog with id {id} not found")

#     blog.delete(synchronize_session=False)
#     db.commit()
#     collection_name.find_one_and_delete({"_id": ObjectId(id)})
#     return 'done'


# def update(id: str, request: schemas.Blog, db: Session):
#     blog = db.query(models.Blog).filter(models.Blog.id == id)
#     blog = collection_name.find_one({"_id": ObjectId(id)})

#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"Blog with id {id} not found")

#     blog.update({"title": request.title, "body": request.body})
#     db.commit()
#     collection_name.find_one_and_update({"_id": ObjectId(id)}, {
#         "$set": dict(request)
#     })
#     return 'updated'


# def show(id: str, db: Session):
#     # blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     blog = collection_name.find_one({"_id": ObjectId(id)})
#     if not blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"Blog with the id {id} is not available")
#     return blog
