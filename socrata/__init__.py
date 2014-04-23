from pickle_warehouse import Warehouse

from socrata.download import download as _download

def metadata(domain, directory):
    'Generate metadata about datasets.'
    warehouse = Warehouse(directory)
    yield from download(warehouse, domain)
