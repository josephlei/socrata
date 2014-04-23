import json
try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

import requests.get

def get(warehouse, url):
    if url in warehouse:
        output = warehouse[url]
    else:
        try:
            response = requests.get(url)
        except Exception as error:
            output = error, response
            warehouse[url] = output
    return output

def page(get, domain, page_number):
    full_url = urljoin(domain, '/api/views?page=%d' % page_number)
    raw = get(full_url, cachedir = directory)
    search_results = json.loads(raw)
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
