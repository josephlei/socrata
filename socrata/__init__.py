from pickle_warehouse import Warehouse

from socrata.download import download as _download

__version__ = '0.0.1'

def metadata(domain, directory = '.socrata'):
    'Generate metadata about datasets.'
    warehouse = Warehouse(directory)
    yield from _download(warehouse, domain)
