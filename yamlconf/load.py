import io

import yaml

from .merge import merge
from .propagate_defaults import propagate_defaults


def load(*files):
    """
    Loads configuration from one or more files by merging right to left.

    :Parameters:
        *files : `file-like`
            A YAML file to read.

    :Returns:
        `dict` : the configuration document
    """
    doc = merge(*(yaml.load(f) for f in files))
    return propagate_defaults(doc)


def loads(*strings):
    """
    Loads configuration from one or more files by merging right to left.

    :Parameters:
        *strings : `str`
            YAML strings to read.

    :Returns:
        `dict` : the configuration document
    """
    return load(*(io.StringIO(s) for s in strings))
