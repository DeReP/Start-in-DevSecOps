'''
Script for getting report of vulnerability scanning of some image from Harbor REST API
'''

from requests import get
from requests.auth import HTTPBasicAuth
from argparse import ArgumentParser
import json

def create_parser():
    parser = ArgumentParser()
    parser.add_argument('--url', required=True)
    parser.add_argument('--user', required=True)
    parser.add_argument('--password', required=True)
    parser.add_argument('--x_accept_vulnerabilities', default='application/vnd.security.vulnerability.report; version=1.1')
    return parser


if __name__ == '__main__':
    parser = create_parser()
    arguments = parser.parse_args()

    headers = {
        'accept': 'application/json',
        'X-Accept-Vulnerabilities': arguments.x_accept_vulnerabilities
    }
   
    response = get(
        url=arguments.url, 
        headers=headers, 
        auth=HTTPBasicAuth(arguments.user, arguments.password))

    result = response.json()
    print(json.dumps(result, indent=4)) 
