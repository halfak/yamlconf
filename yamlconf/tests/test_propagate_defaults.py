from nose.tools import eq_

from ..propagate_defaults import propagate_defaults


def test_propagate_defaults():

    input = {
        'foos': {
            'defaults': {
                'bar': 1,
                'baz': 2
            },
            '1_foo': {},
            '2_foo': {
                'baz': 3
            }
        }
    }
    expected = {
        'foos': {
            'defaults': {
                'bar': 1,
                'baz': 2
            },
            '1_foo': {
                'bar': 1,
                'baz': 2
            },
            '2_foo': {
                'bar': 1,
                'baz': 3
            }
        }
    }
    eq_(propagate_defaults(input), expected)
