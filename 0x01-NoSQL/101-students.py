#!/usr/bin/env python3
"""top_students"""
def top_students(mongo_collection):
    """top_students"""
    new = mongo_collection.aggregate([
        {
            "$project": { 
            "name": "$name" ,
            "averageScore": {"$avg": "$topics.score"}
        }},
        {"$sort": {"averageScore": -1}}
        ])
    return new
