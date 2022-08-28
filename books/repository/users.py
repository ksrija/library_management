from sqlalchemy.orm import Session
from .. import  schemas
from fastapi import HTTPException, status
from ..hashing import Hash
from ..db import collection_book, collection_users
from bson import ObjectId
from datetime import date, timedelta
import re

today = date.today()
end_date = today + timedelta(days=60)

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def create(request: schemas.User):
    # username validation 
    if not re.fullmatch(regex, request.email):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Invalid Email")

    # password hashing
    request.password = Hash.bcrypt(request.password)
    data = dict(request)
    data["books"]=[{"title": "No title","author":"No author","issue_date": "28/08/22","expiry_date": "28/08/22"}]
    collection_users.insert_one(data)
    return data


def show(current_user: schemas.User):
    user = collection_users.find_one({"email": current_user["email"]})
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} is not available")
    return user


def issue(request: schemas.Books, current_user: schemas.User):

    user = collection_users.find_one({"email": current_user["email"]})
    
    data = collection_book.find_one({"title": request.title})
    data["issue_date"]= today.strftime("%d/%m/%Y")
    data["expiry_date"]= end_date.strftime("%d/%m/%Y")

    if "books" in user:
        user["books"].append(data)
    else:
        user["books"]=[data]

    collection_users.find_one_and_update({"email": current_user["email"]}, {
        "$set": user
    })
    return user


def return_book(request,current_user):
    user = collection_users.find_one({"email": current_user["email"]})

    book_list = user["books"]
    if not book_list:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    for book in book_list:
        if book["title"] == request.title:
            book_list.remove(book)
            break
    user["books"] = book_list
    collection_users.find_one_and_update({"email": current_user["email"]}, {
        "$set": user
    })
    return user