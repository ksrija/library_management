from pprint import pprint

from bson import ObjectId
from app.db import collection_requests, collection_book
from app import schemas
import pprint
from datetime import date, timedelta, datetime

today = date.today()


def find_and_update(collection, id, new_dict):
    """Updates the document of a collection with object id with new dictionary.  
    Args:
        collection (database): Collection name  
        id (ObjectId): Object Id of the document in the collection.  
        new_dict (dict()): dictionary of the fields to be changed.  
    """
    collection.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": new_dict
    })

def get_pending():
    coll = collection_requests.find({ "approved": False})
    results = [schemas.RequestPendingResponse.parse_obj(i) for i in coll]
    pprint.pprint(results)
    return results


def get_approved():
    coll = collection_requests.find({"approved": True})
    results = [schemas.RequestPendingResponse.parse_obj(i) for i in coll]
    pprint.pprint(results)
    return results

def approve(id):
    '''takes object id of the request database object and approves'''
    data = collection_requests.find_one({"_id": ObjectId(id)})
    # pprint.pprint(data)
    # data["approved"] = True
    # data["approved_date"] = today.strftime("%d/%m/%Y")
    coll = dict()
    coll["approved"] = True
    coll["approved_date"] = today.strftime("%d/%m/%Y")
    # pprint.pprint(coll)
    find_and_update(collection_requests, id, coll)
    find_and_update(collection_book, data["book_id"],{"available": False})
    return coll
