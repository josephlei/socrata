import os
from time import sleep
import re
import json

from pickle_warehouse import Warehouse


def socrata(url, directory):
    page = 1
    while True:
        full_url = urljoin(url, '/api/views?page=%d' % page)
        filename = os.path.join(directory, re.sub('^https?://', '', full_url))
        raw = get(full_url, cachedir = directory)
        try:
            search_results = json.loads(raw)
        except ValueError:
            os.remove(filename)
            raw = get(full_url, cachedir = directory)
            try:
                search_results = json.loads(raw)
            except ValueError:
                print('**Something is wrong with %s**' % filename)
                break
        else:
            if len(search_results) == 0:
                break
        page += 1
