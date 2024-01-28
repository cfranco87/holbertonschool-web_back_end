#!/usr/bin/env python3
"""Returns a list of schools having a specific topic in a MongoDB collection."""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    - mongo_collection: A pymongo collection object.
    - topic: The topic to search for (string).
    - $in operator, which checks if the specified value 
    (in this case, the topic parameter) is present in the 
    array field ("topics" field in this case)
    """
    return mongo_collection.find({"topics": {"$in": [topic]}})
