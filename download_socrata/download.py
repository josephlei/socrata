import json
import functools
try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

import requests

def get(warehouse, url, requests_get = requests.get):
    if url in warehouse:
        output = warehouse[url]
    else:
        try:
            response = requests_get(url)
        except Exception as error:
            output = error, None
        else:
            output = None, response
        warehouse[url] = output
    error, response = output
    if error == None:
        return response
    else:
        raise error

def page(get, domain_with_scheme, page_number):
    full_url = urljoin(domain_with_scheme, '/api/views?page=%d' % page_number)
    response = get(full_url)
    search_results = json.loads(response.text)
    return search_results

def download(warehouse, domain):
    page_number = 1
    while True:
        search_results = page(functools.partial(get, warehouse), domain, page_number)
        if search_results == []:
            break
        else:
            yield from search_results
            page_number += 1
