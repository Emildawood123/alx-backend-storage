#!/usr/bin/env python3
""" insert by parameter of kwargs """
def insert_school(mongo_collection, **kwargs):
    """ insert function """
    return mongo_collection.insert_one(kwargs).inserted_id
