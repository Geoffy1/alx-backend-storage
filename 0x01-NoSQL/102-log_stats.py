#!/usr/bin/env python3

from pymongo import MongoClient


def print_nginx_request_logs(nginx_collection):
    """Database: logs
    Collection: nginx
    """
    print('{} logs'.format(nginx_collection.count_documents({})))
    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        req_count = nginx_collection.count_documents({'method': method})
        print('\tmethod {}: {}'.format(method, req_count))

    status_checks_count = nginx_collection.count_documents({'method': 'GET', 'path': '/status'})
    print('{} status checks'.format(status_checks_count))

    print('IPs:')
    pipeline = [
        {
            '$group': {
                '_id': '$remote_addr',
                'count': {'$sum': 1},
            },
        },
        {
            '$sort': {'count': -1},
        },
        {
            '$limit': 10,
        },
    ]
    for ip_doc in nginx_collection.aggregate(pipeline):
        print('\t{}: {}'.format(ip_doc['_id'], ip_doc['count']))


def run():
    """Display various attributes
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    print_nginx_request_logs(nginx_collection)


if __name__ == '__main__':
    run()
