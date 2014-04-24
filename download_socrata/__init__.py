from pickle_warehouse import Warehouse as _Warehouse

from download_socrata.download import download as _download

__version__ = '0.0.2'

def metadata(domain, directory = '.socrata'):
    'Generate metadata about datasets.'
    warehouse = _Warehouse(directory)
    yield from _download(warehouse, domain)
