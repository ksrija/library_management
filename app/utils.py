# def find_and_update(collection, id, new_dict):
#     """Updates the document of a collection with object id with new dictionary.  
#     Args:
#         collection (database): Collection name  
#         id (ObjectId): Object Id of the document in the collection.  
#         new_dict (dict()): dictionary of the fields to be changed.  
#     """
#     collection.find_one_and_update({"_id": ObjectId(id)}, {
#         "$set": new_dict
#     })

# def find_one(collection, id):
#     return collection.find_one({"_id": ObjectId(id)})

