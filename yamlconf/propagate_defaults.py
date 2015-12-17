import copy

from .merge import dict_merge_pair


def propagate_defaults(config_doc):
    """
    Propagate default values to sections of the doc.
    """
    for group_name, group_doc in config_doc.items():
        if isinstance(group_doc, dict):
            defaults = group_doc.get('defaults', {})

            for item_name, item_doc in group_doc.items():
                if item_name == 'defaults':
                    continue
                if isinstance(item_doc, dict):

                    group_doc[item_name] = \
                        dict_merge_pair(copy.deepcopy(defaults), item_doc)

    return config_doc
