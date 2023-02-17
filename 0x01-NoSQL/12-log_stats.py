#!/usr/bin/env python3
"""provides some stats about Nginx log stored in MongoDB"""
if __name__ == "__main__":
    import pymongo
    from pymongo import MongoClient

    client = MongoClient("mongodb://localhost:27017")
    logs = client["logs"]
    nginx = logs.nginx

    total = nginx.count_documents({})
    print(f"{total} logs")
    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for i in method:
        print(f"\tmethod {i}: {nginx.count_documents({'method': i})}")
