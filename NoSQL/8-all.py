#!/usr/bin/env python3
"""Python func that list all docs in collection"""

def list_all(mongo_collection):
    """
    list=[] check if list is empty
    if statement to see whats inside of mongo_collection/database
    using .find()
    """
    list = []

    if mongo_collection is not None:
     list = list(mongo_collection.find())
    
    return list
