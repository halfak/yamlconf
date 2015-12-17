from nose.tools import eq_

from ..merge import merge


def test_merge():
    a = {
        'foo': {
            'bar': {
                'foo': 5,
                'bar': 7
            }
        },
        'l': [1, 5, 'foo']
    }
    b = {
        'foo': {
            'bar': {
                'foo': 6
            }
        },
        'bar': 5,
        's': "I'm a string",
        'l': [1, 2, 3]
    }
    c = {
        'foo': {
            'bar': {
                'foobar': 10
            }
        }
    }
    expected = {
        'foo': {
            'bar': {
                'foo': 6,
                'bar': 7,
                'foobar': 10
            }
        },
        'bar': 5,
        's': "I'm a string",
        'l': [1, 2, 3]
    }
    eq_(merge(a, b, c),
        expected)
