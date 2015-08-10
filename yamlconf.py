import copy
import importlib
import io
import sys

import yaml

__version__ = "0.0.5"


def dict_merge(d1, d2):
    """
    Recursively merges values from d2 into d1.
    """
    for key in d2:
        if key in d1 and isinstance(d1[key], dict) and isinstance(d2[key], dict):
                dict_merge(d1[key], d2[key])
        else:
            d1[key] = d2[key]


    return d1


def propagate_defaults(config_doc):
    """
    Propagate default values to to sections of the doc.
    """
    for group_name, group_doc  in config_doc.items():
        if isinstance(group_doc, dict):
            defaults = group_doc.get('defaults', {})

            for item_name, item_doc in group_doc.items():
                if item_name == 'defaults': continue
                if isinstance(item_doc, dict):

                    group_doc[item_name] = dict_merge(copy.deepcopy(defaults),
                                                      item_doc)



    return config_doc

sys.path.insert(0, ".") # Necessary for working in other modules
def import_module(path):
    """
    Import a class from a path.  E.g. import_class("difflib.SequenceMatcher")
    returns a reference to the SequenceMatcher class.
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


def load(f):
    doc = yaml.load(f)
    return propagate_defaults(doc)

def loads(string):
    f = io.StringIO(string)
    return load(f)
