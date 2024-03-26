#!/usr/bin/env python3
""" show all attributes inside collection as para """
def list_all(mongo_collection):
    """show collection"""
    return mongo_collection.find()
