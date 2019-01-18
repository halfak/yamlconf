import io

import yaml

from . import errors
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
    if len(files) == 0:
        raise errors.ConfigError("No config files provided.")
    doc = merge(*(yaml.safe_load(f) for f in files))
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
