#!/usr/bin/env python3
"""adding the top 10 of the most present IPs in the collection nginx of the database logs
"""

from pymongo import MongoClient


def print_nginx_request_logs(nginx_collection):
    """
    Prints stats about Nginx request logs.
    """
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    print("Methods:")
    for method in methods:
        req_count = nginx_collection.count_documents({'method': method})
        print(f"\tmethod {method}: {req_count}")

    status_checks_count = nginx_collection.count_documents(
        {'method': 'GET', 'path': '/status'}
    )
    print(f"{status_checks_count} status checks")


def print_top_ips(server_collection):
    """
    Prints statistics about the top 10 HTTP IPs in a collection.
    """
    pipeline = [
        {'$group': {'_id': "$ip", 'totalRequests': {'$sum': 1}}},
        {'$sort': {'totalRequests': -1}},
        {'$limit': 10},
    ]
    request_logs = server_collection.aggregate(pipeline)

    print("IPs:")
    for request_log in request_logs:
        ip = request_log['_id']
        ip_requests_count = request_log['totalRequests']
        print(f"\t{ip}: {ip_requests_count}")


def run():
    """
    Provides some stats about Nginx logs stored in MongoDB.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    print_nginx_request_logs(nginx_collection)
    print_top_ips(nginx_collection)


if __name__ == '__main__':
    run()
