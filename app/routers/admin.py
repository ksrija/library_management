from typing import List
from fastapi import APIRouter, BackgroundTasks, Depends, status
from app import schemas
from app.repository import books, admin

router = APIRouter(
    prefix="/admin",
    tags=['Admin'],
    # dependencies=[Depends(oauth2.get_current_user)]
)

@router.get("/pending_requests")
def get_pending():
    return admin.get_pending()

@router.get("/approved_requests")
def get_approved():
    return admin.get_approved()

@router.get('/approve', status_code=status.HTTP_200_OK)
def approve(id: str):
    return admin.approve(id)

# Add new book(Admin)
@router.post('/add', status_code=status.HTTP_201_CREATED, response_model=schemas.Books)
def add(request: schemas.Books):
    return books.create(request)

@router.delete('/remove', status_code=status.HTTP_204_NO_CONTENT)
def remove(request: schemas.Books):
    return books.remove(request)