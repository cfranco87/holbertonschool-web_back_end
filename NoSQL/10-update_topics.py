#!/usr/bin/env python3
"""Update the topics of a school in a MongoDB collection"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """
    - mongo_collection: A pymongo collection object.
    - name: The name of the school to be updated.
    - topics: A list of topics to update for the school.
    """
    result = mongo_collection.update_one(
        {"name": name}, {"$set": {"topics": topics}}
        )
    _id = result.upserted_id
    
    return _id