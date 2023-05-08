#!/usr/bin/env python3

from pymongo import MongoClient
from collections import Counter


def print_nginx_request_logs(nginx_collection):
    '''Database: logs
    Collection: nginx
    '''
    # Print the total number of logs
    print('{} logs'.format(nginx_collection.count_documents({})))

    # Print the number of requests by HTTP method
    print('HTTP Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        req_count = nginx_collection.count_documents({'method': method})
        print('\t{}: {}'.format(method, req_count))

    # Print the number of status check requests
    status_checks_count = nginx_collection.count_documents({'method': 'GET', 'path': '/status'})
    print('{} status check requests'.format(status_checks_count))

    # Print the top 10 most present IPs in the collection
    ips = Counter(log['ip'] for log in nginx_collection.find())
    print('Top 10 IPs:')
    for ip, count in ips.most_common(10):
        print('\t{}: {}'.format(ip, count))


def run():
    '''Display various attributes
    '''
    client = MongoClient('mongodb://127.0.0.1:27017')
    print_nginx_request_logs(client.logs.nginx)


if __name__ == '__main__':
    run()
