from collections import namedtuple

import nose.tools as n

import download_socrata.download as dl

def test_page():
    Response = namedtuple('Response', ['text'])
    observed = dl.page(lambda _: Response('[{}]'), 'https://foo.bar', 1)
    n.assert_list_equal(observed, [{}])
