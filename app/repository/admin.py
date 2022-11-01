from pprint import pprint
from app.db import collection_requests
from app import schemas
import pprint


def get_pending():
    coll = collection_requests.find({ "approved": False})
    results = [schemas.RequestPendingResponse.parse_obj(i) for i in coll]
    pprint.pprint(results)
    return results


def get_approved():
    coll = collection_requests.find({ "approved": True})
    results = [schemas.RequestPendingResponse.parse_obj(i) for i in coll]
    pprint.pprint(results)
    return results

def approve(request):
    return 
