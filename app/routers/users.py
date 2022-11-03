from typing import List, Optional
from fastapi import APIRouter

from app import oauth2
from app import schemas
from fastapi import APIRouter,Depends
from app.repository import users


router = APIRouter(
    prefix="/user",
    tags=['Users']
)

@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User):
    return users.create(request)

@router.get('/profile',response_model=schemas.ShowUser)
def get_user(current_user: schemas.User = Depends(oauth2.get_current_user)):
    return users.show(current_user)

@router.get('/show_requests')
def show_request(current_user: schemas.User = Depends(oauth2.get_current_user)):
    return users.show_request(current_user)


@router.put("/request", response_model=schemas.RequestPendingResponse)
def request_book(request: schemas.RequestBase,current_user: schemas.User = Depends(oauth2.get_current_user)):
    return users.request(request,current_user)

@router.put("/issue", response_model=schemas.ShowUser)
def issue_book(request: schemas.Books,current_user: schemas.User = Depends(oauth2.get_current_user)):
    return users.issue(request,current_user)


@router.put("/return", response_model=schemas.ShowUser)
def return_book(request: schemas.Books,current_user: schemas.User = Depends(oauth2.get_current_user)):
    return users.return_book(request,current_user)

