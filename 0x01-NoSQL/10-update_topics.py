#!/usr/bin/env python3
"""
updates all documents' topics based on the name provided
"""


def update_topics(mongo_collection, name, topics):
    """updates all documents in mongo_collection based on name"""
    mongo_collection.update_all({"name": name}, {"$set": {"topics": topics}})
