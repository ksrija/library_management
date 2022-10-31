from typing import List, Optional
from fastapi import APIRouter, Depends, status, HTTPException
from app import schemas, oauth2
from app.repository import books, users

router = APIRouter(
    prefix="/books",
    tags=['Books'],
    # dependencies=[Depends(oauth2.get_current_user)]
)

# Show all books
@router.get('/', response_model=List[schemas.ShowBooks])
def all():
    return books.get_all()

# Show all users
@router.get('/users', response_model=List[schemas.ShowUser])
def show_users():
    return books.show_users()


# Show all books
@router.get('/search')
def search_filter(query: Optional[str]):
    return users.search_all(query)

# Add new book(Admin)
@router.post('/add', status_code=status.HTTP_201_CREATED, response_model=schemas.Books)
def add(request: schemas.Books):
    return books.create(request)


@router.delete('/remove', status_code=status.HTTP_204_NO_CONTENT)
def remove(request: schemas.Books):
    return books.remove(request)


# @router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
# def update(id: str, request: schemas.books, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
#     return books.update(id, request, db)


# @router.get('/{id}', status_code=200, response_model=schemas.Showbooks)
# def show(id: str, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
#     return books.show(id, db)
