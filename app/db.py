from pymongo import MongoClient

# by default connect to the local host
conn = MongoClient(
    'mongodb+srv://srija:EIbN4LlyqFyRZfcQ@cluster0.jg7b3zi.mongodb.net/?retryWrites=true&w=majority')


db = conn.library

collection_book = db["books"]
collection_users = db["users"]

collection_requests = db["requests"]