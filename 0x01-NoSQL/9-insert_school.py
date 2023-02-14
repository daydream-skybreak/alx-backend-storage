#!/usr/bin/env python3
"""
module to insert a new document to a collection
"""


def insert_school(mongo_collection, **kwargs):
    """inserts a new document to mongo_collection
    :returns the id of the document inserted
    """
    return mongo_collection.insert_one(kwargs).inserted_id
