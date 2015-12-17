import os

from nose.tools import eq_

from ..load import load, loads

EXPECTED = {
    'hats': {
        'red': {
            'color': "red",
            'size': 10
        },
        'bowler': {
            'color': "black",
            'size': 35
        }
    }
}

PWD = os.path.dirname(os.path.realpath(__file__))


def test_load():

    eq_(load(open(os.path.join(PWD, 'config1.yaml')),
             open(os.path.join(PWD, 'config2.yaml'))),
        EXPECTED)

    eq_(loads(open(os.path.join(PWD, 'config1.yaml')).read(),
              open(os.path.join(PWD, 'config2.yaml')).read()),
        EXPECTED)
