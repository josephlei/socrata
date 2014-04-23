from collections import namedtuple

import nose.tools as n

import socrata.download as dl

def test_get_success():
    fake_warehouse = {}
    url = 'http://a.b/c'
    expected_response = 88
    observed_response = dl.get(fake_warehouse, url, requests_get = lambda _: int(expected_response))
    n.assert_equal(observed_response, expected_response)
    n.assert_tuple_equal(fake_warehouse[url], (None, expected_response))

def test_get_error():
    fake_warehouse = {}
    url = 'http://a.b/c'

    error = ValueError('This is a test.')
    def fake_get(_):
        raise error

    try:
        dl.get(fake_warehouse, url, requests_get = fake_get)
    except ValueError:
        n.assert_tuple_equal(fake_warehouse[url], (error, None))
    else:
        raise AssertionError('An error should have been raised.')

def test_page():
    Response = namedtuple('Response', ['text'])
    observed = dl.page(lambda _: Response('[{}]'), 'https://foo.bar', 1)
    n.assert_list_equal(observed, [{}])
