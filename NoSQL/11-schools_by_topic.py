#!/usr/bin/env python3
"""Returns a list of schools having a specific topic in a MongoDB collection."""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    - mongo_collection: A pymongo collection object.
    - topic: The topic to search for (string).
    - Using the find method to query documents with the specified topic
    """
    folder = mongo_collection({"topics": topic})
    
    """ Extracting the list of schools from the cursor"""
    school_list = [document["name"] for document in folder]

    return school_list
