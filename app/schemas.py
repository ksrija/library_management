from typing import List, Optional
from pydantic import BaseModel, constr, EmailStr, Field

MobileStr = constr(regex = r'^\d{10}$') 

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
    email: EmailStr
    password:str
    # mobile: int = Field()

class ShowUser(BaseModel):
    name:str
    email:str
    # mobile:MobileStr
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