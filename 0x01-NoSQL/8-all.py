#!/usr/bin/env python3
"""
a module to work with mongodb collection
@method: list_all
        :returns the documents in the collection passed
"""


def list_all(mongo_collection):
    """returns a list of the mongo collection"""
    coll = mongo_collection.find()
    coll_list = list(coll)
    if len(coll) == 0:
        return []
    return coll
