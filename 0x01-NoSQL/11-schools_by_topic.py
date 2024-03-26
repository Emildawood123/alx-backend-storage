#!/usr/bin/env python3
"""find with ele in list"""
def schools_by_topic(mongo_collection, topic):
    """find with ele in list"""
    return mongo_collection.find({topics.topic: "Python"})
