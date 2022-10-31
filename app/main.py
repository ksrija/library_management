from fastapi import FastAPI
from app.routers import authentication,books,users
from mangum import Mangum

app = FastAPI(root_path="")   #DEV


app.include_router(authentication.router)
app.include_router(books.router)
app.include_router(users.router)


@app.get("/")
def show():
    return{"data":"Welcome to library!"}