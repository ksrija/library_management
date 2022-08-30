from sqlalchemy.orm import Session
from .. import  schemas
from fastapi import HTTPException, status
# from ..dependency import users
from ..db import collection_book, collection_users

# from bson import ObjectId


def get_all():
    blogs = list(collection_book.find())
    return blogs

# does not make sense for books
def show_users():
    users = [doc for doc in collection_users.find()]
    return users


def create(request: schemas.Books):
    data = dict(request)
    collection_book.insert_one(data)
    return request


def remove(request):
    book = collection_book.find_one(dict(request))
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Book with title: {request.title} not found")

    collection_book.find_one_and_delete(dict(request))
    return 'deleted'


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
