#!/usr/bin/env python3
""" insert by parameter of kwargs """
def insert_school(mongo_collection, **kwargs):
    """ insert function """
    return mongo_collection.insertOne(kwargs).inserted_id
