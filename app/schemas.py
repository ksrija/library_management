from datetime import datetime
from optparse import Option
from typing import List, Optional, Union
from bson import ObjectId
from pydantic import BaseModel, constr, EmailStr, Field


from bson.objectid import ObjectId as BsonObjectId


MobileStr = constr(regex = r'^\d{10}$') 


class ObjectIdStr(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, ObjectId):
            raise ValueError("Not a valid ObjectId")
        return str(v)

class PydanticObjectId(BsonObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, BsonObjectId):
            raise TypeError('ObjectId required')
        return str(v)


class PyObjectId(ObjectId):

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid objectid')
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type='string')
        
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

class RequestBase(BaseModel):
    title: str
    author: str 

class RequestPendingResponse(BaseModel):
    user_id: PyObjectId=None
    book_id:PyObjectId=None
    request_date: Union[str, None] = None
    # approved_date:Union[str, None] = None
    approved: bool
    class Config():
        orm_mode = True
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }


class RequestApprovedResponse(RequestPendingResponse):
    approved_date:Union[str, None] = None
    class Config():
        orm_mode = True
    