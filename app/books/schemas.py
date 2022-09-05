from typing import List, Optional
from pydantic import BaseModel, constr

EntryCode = constr(regex=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

class BooksBase(BaseModel):
    title: str
    author: str

class Books(BooksBase):
    class Config():
        orm_mode = True

class UserBooks(BaseModel):
    title: str
    author:str
    issue_date: str
    expiry_date: str

    class Config():
        orm_mode=True

class User(BaseModel):
    name: str
    email: EntryCode
    password:str

class ShowUser(BaseModel):
    name:str
    email:str
    books : List[UserBooks] =[]
    class Config():
        orm_mode = True

class ShowBooks(BaseModel):
    title: str
    author:str
    # creator: ShowUser

    class Config():
        orm_mode = True


class Login(BaseModel):
    username: str
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None


class ShowMyBook(BaseModel):
    title: str
    author:str

    class Config():
        orm_mode = True