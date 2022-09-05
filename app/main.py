from fastapi import FastAPI
# from . import  models
# from .database import engine
# from .books.routers import books, users, authentication
from books.routers import books, users, authentication
from mangum import Mangum

app = FastAPI()


app.include_router(authentication.router)
app.include_router(books.router)
app.include_router(users.router)

handler = Mangum(app)