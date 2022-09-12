from passlib.context import CryptContext
from passlib.hash import bcrypt
pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    def bcrypt(password: str):
        print("BACKEND: ",bcrypt.get_backend())
        return bcrypt.hash("password")
        # return pwd_cxt.hash(password)

    def verify(hashed_password,plain_password):
        return bcrypt.verify(plain_password, hashed_password)
        # return pwd_cxt.verify(plain_password,hashed_password)