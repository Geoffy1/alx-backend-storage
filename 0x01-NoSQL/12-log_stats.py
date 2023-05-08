#!/usr/bin/env python3
"""
Provides some stats about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient


if __name__ == "__main__":
    # Connect to MongoDB
    client = MongoClient()
    logs = client.logs.nginx

    # Count number of documents
    count = logs.count_documents({})

    # Count number of documents with each method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    methods_count = {method: logs.count_documents({"method": method}) for method in methods}

    # Count number of documents with method=GET and path=/status
    status_check_count = logs.count_documents({"method": "GET", "path": "/status"})

    # Print stats
    print(f"{count} logs")
    print("Methods:")
    for method in methods:
        print(f"    method {method}: {methods_count[method]}")
    print(f"{status_check_count} status check")

