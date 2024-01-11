#!/usr/bin/env python3
"""Python func that list all docs in collection based on kwargs"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    _id = will hold mongo_collection, inside mongo is kwargs
    mongo_collection is a pymongo collection object
    """
    _id = mongo_collection.insert_one(kwargs)
    return _id
