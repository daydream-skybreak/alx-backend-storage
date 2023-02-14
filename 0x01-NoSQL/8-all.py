#!/usr/bin/python3
"""
a module to work with mongodb collection
@method: list_all
        :returns the documents in the collection passed
"""


def list_all(mongo_collection):
    if mongo_collection.count():
        return []
    return [i for i in mongo_collection.find()]
