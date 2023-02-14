#!/usr/bin/env python3
"""
gets schools with a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """ :returns documents whose topics contain topic"""
    result = []
    for i in mongo_collection.find():
        if topic in i.get('topics'):
            result.append(i)

    return result
