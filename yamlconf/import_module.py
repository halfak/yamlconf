import importlib


def import_module(path):
    """
    Import a class or module from a path.  E.g.
    ``import_class("difflib.SequenceMatcher")`` returns a reference to the
    SequenceMatcher class.
    """
    try:
        parts = path.split(".")
        module_path = ".".join(parts[:-1])
        attribute_name = parts[-1]

        module = importlib.import_module(module_path)

        attribute = getattr(module, attribute_name)

        return attribute
    except AttributeError:
        return importlib.import_module(path)
