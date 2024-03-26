#!/usr/bin/env python3
"""count method and status inide docs"""
from pymongo import MongoClient


def methods_count():
    """count method"""
    mon = MongoClient("mongodb://127.0.0.1:27017")
    collection = mon.logs.nginx
    All = collection.count_documents({})
    print("{} logs".format(All))
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))
    status = collection.count_documents({"method": "GET", "path": "/status"})
    print("{} status check".format(status))
    ips = collection.aggregate(
        [
            {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
            {"$sort": {"count": -1}},
            {"$limit": 10},
        ]
    )
    print("IPs:")
    for ip in ips:
        print('\t{}: {}'.format(ip.get('_id'), ip.get("count")))
if __name__ == "__main__":
    methods_count()
