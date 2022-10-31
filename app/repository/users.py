from ast import keyword
import re
from app import  schemas
from fastapi import HTTPException, status
from app.hashing import Hash
from app.db import collection_book, collection_users
from bson import ObjectId
from datetime import date, timedelta

today = date.today()
end_date = today + timedelta(days=60)


def create(request: schemas.User):
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


def search_all(query):

    result = re.compile('{}'.format(query), re.I)
    results = collection_book.find({ "title": {'$regex': result}})
    # print(results)
    books = []
    for book in results:
        books.append(schemas.ShowBooks.parse_obj(book))

    
    return books