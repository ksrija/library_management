from sqlalchemy.orm import Session
from .. import  schemas
from fastapi import HTTPException, status
from ..hashing import Hash
from ..db import collection_book, collection_users
from bson import ObjectId
from datetime import date, timedelta

today = date.today()
end_date = today + timedelta(days=60)

# temp_id = "6307ea5c8c338e29979a96ee"

def create(request: schemas.User):
    request.password = Hash.bcrypt(request.password)
    data = dict(request)
    data["books"]=[]
    collection_users.insert_one(data)
    return data


def show(current_user: schemas.User):
    print(current_user)

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
