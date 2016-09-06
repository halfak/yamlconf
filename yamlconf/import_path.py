import importlib
import sys


def import_path(path):
    """
    Imports any valid python module or attribute path as though it were a
    module

    :Example:
        >>> from yamlconf import import_path
        >>> from my_package.my_module.my_submodule import attribute
        >>> attribute.sub_attribute == \
        ...     import_path("y_package.my_module.my_submodule.attribute.sub_attribute")
        True
        >>>

    :Parameters:
        path : `str`
            A valid python path that crosses modules and/or attributes
    """  # noqa
    sys.path.insert(0, ".")
    parts = path.split(".")
    module = None

    # Import the module as deeply as possible.  Prioritize an attribute chain
    # over a module chain
    for i in range(1, len(parts)+1):
        if module is not None and hasattr(module, parts[i-1]):
            try:
                return _import_attributes(module, parts[i-1:])
            except AttributeError:
                pass
        module_path = ".".join(parts[0:i])
        module = importlib.import_module(module_path)

    return module


def _import_attributes(module, attributes):
    for attribute in attributes:
        module = getattr(module, attribute)

    return module
