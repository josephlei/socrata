import json
import functools
try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

import requests
from picklecache import downloader

def page(get, domain_with_scheme, page_number):
    full_url = urljoin(domain_with_scheme, '/api/views?page=%d' % page_number)
    response = get(full_url)
    search_results = json.loads(response.text)
    return search_results

def download(warehouse, domain):
    page_number = 1
    get = downloader(requests.get, warehouse)
    while True:
        search_results = page(get, domain, page_number)
        if search_results == []:
            break
        else:
            yield from search_results
            page_number += 1
