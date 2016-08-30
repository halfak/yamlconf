import importlib


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
    """
    parts = path.split(".")
    module = None
    module_i = 0

    # Import the module as deeply as possible
    try:
        for i in range(1, len(parts)+1):
            module_path = ".".join(parts[0:i])
            module = importlib.import_module(module_path)
            module_i = i
    except ImportError:
        if module is None:
            raise
        else:
            pass

    module_or_attribute = module
    for attribute_name in parts[module_i:]:
        module_or_attribute = getattr(module_or_attribute, attribute_name)

    return module_or_attribute
