Yaml Configuration
==================

This library provides a means to read yaml configuration files and propagate
default values in reasonable ways.  Nothing complicated.

* **Installation:** ``pip install yamlconfig``

:Example:

    >>> import yamlconf
    >>>
    >>> doc = yamlconf.loads("""
    ... test: demo_test
    ...
    ... tests:
    ...     defaults:
    ...         foo: 5
    ...     demo_test:
    ...         bar: 6
    ... """)
    >>>
    >>> doc['tests'][doc['test']]['foo']
    5
    >>> doc['tests'][doc['test']]['bar']
    6

:Functions:

* load(*file-like*) : Returns a *dict* with defaults propagated
* loads(*string*) : Returns a *dict* with defaults propagated
* load_module(*class-path*) : Imports and returns
